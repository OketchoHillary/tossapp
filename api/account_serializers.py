from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.db.models import F
from django_countries import Countries

from rest_framework import serializers, exceptions

from accounts.admin import validate_phone_number
from accounts.models import *
from accounts.utils import generate_verification_code


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
    password = serializers.CharField()
    referrer_share_code = serializers.CharField()
    sex = serializers.ChoiceField(choices=GENDER_CHOICES)

    def create(self, validated_data):
        code = generate_verification_code()
        phone_number = validated_data['phone_number']
        referrer_share_code = validated_data['referrer_share_code']

        # verifying referrer share code

        if len(Tuser.objects.filter(share_code=referrer_share_code)) == 0:
            raise exceptions.ValidationError("Please provide a valid Referral code or leave the field blank")
        else:
            referrer = Tuser.objects.get(share_code=validated_data["referrer_share_code"])
            sponsor_id = referrer.id

            # incrementing points on referee
            Tuser.objects.filter(id=sponsor_id).update(points=F("points") + 1)

        # verifying phone number
        if not validate_phone_number(phone_number):
            raise exceptions.ValidationError("Please provide a valid MTN or Airtel number")
        elif phone_number.startswith('0'):
            phone_number = phone_number.replace('0','256',1)
        elif phone_number.startswith('+256'):
            phone_number = phone_number.replace('+256', '256', 1)
        user = Tuser(username=validated_data['username'], sex=validated_data['sex'], phone_number=phone_number,
                     verification_code=code, is_active=False, referrer_id=sponsor_id)
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
        exclude = ['is_admin', 'is_active', 'share_code', 'verification_code', 'password']


class ChangePasswordSerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ChangePasswordSerializer, self).__init__(*args, **kwargs)

    old_password = serializers.CharField()
    new_password1 = serializers.CharField()
    new_password2 = serializers.CharField()


class ProfilePicSerializer(serializers.Serializer):
    class Meta:
        model = Tuser
        fields = ['id', 'profile_photo']