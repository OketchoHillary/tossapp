from django.contrib.auth import authenticate
from django_countries import Countries

from rest_framework import serializers, exceptions

from accounts.models import *
from accounts.utils import generate_verification_code


class SerializableCountryField(serializers.ChoiceField):
    def __init__(self, **kwargs):
        super(SerializableCountryField, self).__init__(choices=Countries())

    def to_representation(self, value):
        if value in ('',  None):
            return ''
        return super(SerializableCountryField, self).to_representation(value)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuser
        fields = ('username', 'phone_number', 'sex', 'password')

    def create(self,  validated_data):
        code = generate_verification_code()
        phone_number = validated_data['phone_number']
        if phone_number.startswith('0'):
            phone_number = phone_number.replace('0','256',1)
        user = Tuser(username=validated_data['username'], sex=validated_data['sex'], phone_number=phone_number,
                     verification_code=code, is_active=False)
        user.set_password(validated_data['password'],)
        user.save()
        return user


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


class UserProfileSerializer(serializers.ModelSerializer):
    country = SerializableCountryField(allow_blank=True)

    class Meta:
        model = Tuser
        fields = '__all__'