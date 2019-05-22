# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework import generics, permissions, status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, mixins
from api.account_serializers import *
from api.permissions import IsOwnerOrReadOnly
from tossapp.models import Notification


class UserCreate(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        new_user = UserSerializer(data=request.data)
        if new_user.is_valid():
            new_user.save(is_agreed=True)
            return Response({'code': 1, 'response': new_user.data}, status=status.HTTP_201_CREATED)
        return Response({'code': 0, 'response': new_user.errors}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token':token.key, 'message':"Login successful"}, status=200)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication)

    def post(self, request):
        django_logout(request)
        return Response(status=204)


class ProfileView(generics.RetrieveAPIView, mixins.RetrieveModelMixin):
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user


class ProfileUpdateView(generics.RetrieveUpdateAPIView, mixins.UpdateModelMixin):
    queryset = Tuser.objects.all()
    serializer_class = EditProfileSerializer

    def get_object(self):
        return self.request.user


class ProfilePicViewSet(generics.RetrieveUpdateAPIView, mixins.UpdateModelMixin):
    queryset = Tuser.objects.all()
    serializer_class = ProfilePicSerializer

    def get_object(self):
        return self.request.user


class VerificationAPI(viewsets.ViewSet):
    authentication_classes = ()
    permission_classes = ()

    def get_verification_code(self, request, username):
        response = []
        verifier = Tuser.objects.filter(username=username).values_list('verification_code')[0]
        veri = {
            'verification_code':verifier
        }
        response.append(veri)
        return Response({'response': response}, status=status.HTTP_200_OK)

    def verify_user(self, request, username):
        this_user = Tuser.objects.get(username=username)
        activate_me = ActivateSerializer(data=request.data, user=this_user)
        activate_me.is_valid()
        verification_code = activate_me.validated_data["verification_code"]
        if verification_code == this_user.verification_code and not this_user.is_active:
            this_user.is_active = True
            this_user.save()
            django_login(request, this_user)
            this_user.verification_code = generate_verification_code()
            this_user.save()
            token, created = Token.objects.get_or_create(user=this_user)
            sponsor_id = this_user.referrer.id
            Tuser.objects.filter(id=sponsor_id).update(referrer_prize=F("referrer_prize") + Tuser.REFERRAL_PRIZE,
                                                       balance=F("balance") + Tuser.REFERRAL_PRIZE)
            return Response({"token": token})
        else:
            return Response({"error": "Wrong Verification code"}, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordAPI(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def pass_change(self, request):
        this_user = request.user
        my_pass = ChangePasswordSerializer(data=request.data, user=this_user)
        my_pass.is_valid()
        old_password = my_pass.validated_data["old_password"]
        new_password1 = my_pass.validated_data["new_password1"]
        new_password2 = my_pass.validated_data["new_password2"]
        if not this_user.check_password(old_password):
            raise serializers.ValidationError('Incorrect password.')
        elif new_password1 and new_password2 and new_password1 != new_password2:
            raise serializers.ValidationError("Passwords don't match")
        else:
            this_user.set_password(new_password1)
            this_user.save()
            messages.success(request, 'Successfully changed password')
            Notification.objects.create(user=self.request.user, title='Password', description='Password has been changed',
                                        type=0)
            return Response({'code': 1, 'response': 'Successfully changed password'})


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})