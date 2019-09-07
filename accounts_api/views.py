# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.contrib.auth import login as django_login, logout as django_logout, logout
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.http import HttpResponseRedirect
from rest_framework import generics, status
from django.core import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, mixins
from accounts_api.account_serializers import *
from tossapp_api.models import Notification


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
        return Response({'token': token.key, 'message': "Login successful"}, status=200)


class LogoutView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=204)


class ProfileView(APIView):
    serializer_class = UserProfileSerializer
    queryset = Tuser.objects.all()

    def get(self, request):
        ref_details = {
            'rank': request.user.refferal_ranking,
            'username': request.user.username,
            'name': request.user.get_my_full_name(),
            'gender': request.user.sex,
            'location': request.user.address,
            # 'country': request.user.country,
            'phone_number': request.user.phone_number,
            'balance': request.user.balance,
        }

        return Response({'response': ref_details}, status=status.HTTP_200_OK)


class ProfileUpdateView(generics.RetrieveUpdateAPIView, mixins.UpdateModelMixin):
    queryset = Tuser.objects.all()
    serializer_class = EditProfileSerializer

    def get_object(self):
        return self.request.user


class UsernameUpdateView(generics.RetrieveUpdateAPIView, mixins.UpdateModelMixin):
    queryset = Tuser.objects.all()
    serializer_class = ChangeUsernameSerializer

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
            if this_user.referrer:
                sponsor_id = this_user.referrer.id
                Tuser.objects.filter(id=sponsor_id).update(referrer_prize=F("referrer_prize") + Tuser.REFERRAL_PRIZE,
                                                           balance=F("balance") + Tuser.REFERRAL_PRIZE)
            else:
                pass
            return Response({"token": token.key})
        else:
            return Response({"error": "Wrong Verification code"}, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordAPI(viewsets.ViewSet):

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
            Notification.objects.create(user=self.request.user, title='Password',
                                        description='Password has been changed',type=0)
            return Response({'code': 1, 'response': 'Successfully changed password'})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


class ForgotPassword(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        password_rese = ForgotPassSerializer(data=request.data)
        if password_rese.is_valid():
            mobile = password_rese.validated_data["phone_number"]
            user = Tuser.objects.get(phone_number=mobile)
            if Reset_password.objects.filter(user=user).count() == 0:
                Reset_password.objects.create(user=user)
            else:
                Reset_password.objects.update(user=user, password_reset=pass_res_code())
            sms.send("Tossapp Password reset code: " + str(pass_res_code()), [proper_dial(mobile)])
            return Response({'code': 1, 'response': password_rese.data}, status=status.HTTP_200_OK)
        return Response({'code': 0, 'response': password_rese.errors}, status=status.HTTP_400_BAD_REQUEST)


class ResetCode(viewsets.ViewSet):
    authentication_classes = ()
    permission_classes = ()

    def post_code(self, request, username):
        this_user = Tuser.objects.get(username=username)
        code = EnterResetSerializer(data=request.data)
        if code.is_valid():
            reset_code = code.validated_data['reset_code']
            print(reset_code)
            return Response({'code': 1, 'response': code.data}, status=status.HTTP_200_OK)
        return Response({'code': 0, 'response': code.errors}, status=status.HTTP_400_BAD_REQUEST)


class PasswordReset(viewsets.ViewSet):
    authentication_classes = ()
    permission_classes = ()

    def reset_pass(self, request, username):
        this_user = Tuser.objects.get(username=username)
        pass_reset = RestePassword(data=request.data)
        if pass_reset.is_valid():
            password = pass_reset.validated_data['password']
            confirm_password = pass_reset.validated_data['confirm_password']
            print(password)
            return Response({'code': 1, 'response': pass_reset.data}, status=status.HTTP_200_OK)
        return Response({'code': 0, 'response': pass_reset.errors}, status=status.HTTP_400_BAD_REQUEST)


class ResendCode(viewsets.ViewSet):
    authentication_classes = ()
    permission_classes = ()

    def resend_code(self, request, username):
        this_user = Tuser.objects.get(username=username)
        Tuser.objects.filter(username=username).update(verification_code=generate_verification_code())
        # sms.send("Tossapp Verification code: " + str(this_user.verification_code), [this_user.phone_number])
        return Response({'code': 1}, status=status.HTTP_200_OK)
