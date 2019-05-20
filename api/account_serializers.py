from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.db.models import F
import datetime
from django_countries import Countries

from rest_framework import serializers, exceptions

from accounts.admin import validate_phone_number
from accounts.models import *
from accounts.utils import generate_verification_code


def proper_dial(phone):
    if phone.startswith('0'):
        phone = phone.replace('0', '256', 1)
    elif phone.startswith('+256'):
        phone = phone.replace('+256', '256', 1)
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
            raise serializers.ValidationError("Please provide a valid username or leave the field blank")
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
            raise exceptions.ValidationError('This Phone number is already in use.')

        my_age = int((datetime.date.today() - dob).days / 365.25)

        if my_age < 18:
            raise exceptions.ValidationError('Only those above 18 years can Signup')

        # incrementing points on referee

        user = Tuser(username=validated_data['username'], sex=validated_data['sex'], dob=dob, phone_number=phone_number,
                     verification_code=generate_verification_code(), is_active=False, is_agreed=True)
        if referrer_share_code != "":
            referrer = Tuser.objects.get(share_code=validated_data["referrer_share_code"])
            user.referrer = referrer
            Tuser.objects.filter(id=referrer.id).update(points=F("points") + 1)
        user.phone_number = proper_dial(phone_number)
        user.set_password(validated_data['password'],)
        user.save()
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
                    raise exceptions.ValidationError(msg)
            else:
                msg = 'User does not exist'
                raise exceptions.ValidationError(msg)
        else:
            msg = "Wrong Username or Password"
            raise exceptions.ValidationError(msg)
        return data


class ActivateSerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ActivateSerializer, self).__init__(*args, **kwargs)

    verification_code = serializers.CharField()

    def validate(self, data):
        verification_code = data.get("verification_code", "")

        return data


class UserProfileSerializer(serializers.ModelSerializer):
    country = SerializableCountryField(allow_blank=True)

    class Meta:
        model = Tuser
        exclude = ['is_admin', 'is_active', 'share_code', 'verification_code', 'password', 'timestamp', 'last_login']


class EditProfileSerializer(serializers.ModelSerializer):
    country = SerializableCountryField(allow_blank=True)
    address = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)

    class Meta:
        model = Tuser
        fields = ['username', 'first_name', 'last_name', 'sex', 'phone_number', 'country', 'address']

    def validate(self, validated_data):
        username = validated_data['username']
        phone_number = validated_data['phone_number']

        # verifying phone number
        if not validate_phone_number(phone_number):
            raise exceptions.ValidationError("Please provide a valid MTN or Airtel number")
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