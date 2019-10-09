from django.contrib.auth import authenticate
import datetime
from django_countries.serializers import CountryFieldMixin
from django_countries import Countries

from rest_framework import serializers, exceptions

from accounts_api.admin import validate_phone_number
from accounts_api.models import *
from accounts_api.utils import generate_verification_code
from tossapp_api.sms_setting import sms


def proper_dial(phone):
    if phone.startswith('0'):
        phone = phone.replace('0', '+256', 1)
    elif phone.startswith('256'):
        phone = phone.replace('256', '+256', 1)
    return phone


class SerializableCountryField(serializers.ChoiceField):
    def __init__(self, **kwargs):
        super(SerializableCountryField, self).__init__(choices=Countries())

    def to_representation(self, value):
        if value in ('',  None):
            return ''
        return super(SerializableCountryField, self).to_representation(value)


class UserSerializer(serializers.Serializer):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    phone_number = serializers.CharField()
    username = serializers.CharField()
    dob = serializers.DateField(required=True)
    password = serializers.CharField()
    referrer_share_code = serializers.CharField(required=False, allow_blank=True)
    sex = serializers.ChoiceField(choices=GENDER_CHOICES)

    def clean_referrer(self, validated_data):
        referrer_share_code = validated_data['referrer_share_code']
        if len(Tuser.objects.filter(share_code=referrer_share_code)) == 0:
            raise serializers.ValidationError("Please provide a valid share code or leave the field blank")
        return referrer_share_code

    def create(self, validated_data):
        username = validated_data['username']
        dob = validated_data['dob']
        phone_number = validated_data['phone_number']
        referrer_share_code = validated_data['referrer_share_code']

        # Checking for username
        qs = Tuser.objects.filter(username=username)
        if qs.count() > 0:
            raise exceptions.ValidationError('This username is already in use.')

        # verifying phone number
        if not validate_phone_number(phone_number):
            raise exceptions.ValidationError("Please provide a valid MTN or Airtel number")

        qn = Tuser.objects.filter(phone_number=phone_number)
        if qn.count() > 0:
            raise serializers.ValidationError('This Phone number is already in use.')

        my_age = int((datetime.date.today() - dob).days / 365.25)

        if my_age < 18:
            raise serializers.ValidationError('Only those above 18 years can Signup')

        # incrementing points on referee

        user = Tuser(username=username, sex=validated_data['sex'], dob=dob,
                     verification_code=generate_verification_code(), is_active=False, is_agreed=True)

        user.phone_number = proper_dial(phone_number)
        user.set_password(validated_data['password'],)
        user.save()
        sms.send("Tossapp verification code: "+str(user.verification_code), [proper_dial(phone_number)])
        return validated_data


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = 'account not yet activated'
                    raise serializers.ValidationError(msg)
            else:
                msg = "Wrong Username or Password"
                raise serializers.ValidationError(msg)
        else:
            msg = "Wrong Username or Password"
            raise serializers.ValidationError(msg)
        return data


class ActivateSerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ActivateSerializer, self).__init__(*args, **kwargs)

    verification_code = serializers.CharField()

    def validate(self, data):
        verification_code = data.get("verification_code")

        return data


class UserProfileSerializer(CountryFieldMixin, serializers.ModelSerializer):
    country = serializers.CharField()

    class Meta:
        model = Tuser
        exclude = ['is_admin', 'is_active', 'share_code', 'verification_code', 'password', 'timestamp', 'last_login']


class EditProfileSerializer(serializers.ModelSerializer):
    country = SerializableCountryField(allow_blank=True)
    address = serializers.CharField(required=False, allow_blank=True)
    first_name = serializers.CharField(required=False, allow_blank=True)
    last_name = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Tuser
        fields = ['first_name', 'last_name', 'sex', 'dob', 'country', 'address']

    def validate(self, validated_data):
        dob = validated_data['dob']

        my_age = int((datetime.date.today() - dob).days / 365.25)

        if my_age < 18:
            raise serializers.ValidationError('Only those above 18 years can Signup')

        return validated_data


class ChangeUsernameSerializer(serializers.ModelSerializer):
    old_username = serializers.CharField()
    new_username = serializers.CharField()

    class Meta:
        model = Tuser
        fields = ['username']


class ChangePhoneNumberSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField()

    class Meta:
        model = Tuser
        fields = ['phone_number']

    def validate(self, validated_data):
        phone_number = validated_data['phone_number']

        # verifying phone number
        if not validate_phone_number(phone_number):
            raise serializers.ValidationError("Please provide a valid MTN or Airtel number")
        proper_dial(phone_number)

        return validated_data


class ChangePasswordSerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ChangePasswordSerializer, self).__init__(*args, **kwargs)

    old_password = serializers.CharField()
    new_password1 = serializers.CharField()
    new_password2 = serializers.CharField()


class ProfilePicSerializer(serializers.ModelSerializer):
    profile_photo = serializers.ImageField(required=True)

    class Meta:
        model = Tuser
        fields = ['profile_photo']


class ForgotPassSerializer(serializers.Serializer):
    phone_number = serializers.CharField()

    def validate(self, validated_data):
        phone_number = validated_data['phone_number']
        this_number = proper_dial(phone_number)
        # verifying phone number
        if not validate_phone_number(this_number):
            raise serializers.ValidationError("Please provide a valid MTN or Airtel number")
        if Tuser.objects.filter(phone_number=this_number).count() == 0:
            raise serializers.ValidationError("No user with Phone number exists")
        return validated_data


class EnterResetSerializer(serializers.Serializer):
    reset_code = serializers.CharField(required=True)


class RestePassword(serializers.Serializer):
    code = serializers.CharField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()