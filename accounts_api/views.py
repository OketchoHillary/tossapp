# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.contrib.auth import login as django_login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from django.core import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, mixins
from accounts_api.account_serializers import *
from accounts_api.utils import reset_code
from tossapp_api.models import Notification


class UserCreate(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        new_user = UserSerializer(data=request.data)
        if new_user.is_valid():
            x = new_user.save(is_agreed=True)
            request.session['tusername'] = x['username']
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


class UsernameUpdateView(viewsets.ViewSet):

    def get_username(self, request):
        user = get_object_or_404(Tuser, id=request.user.id)
        myusername = user.username
        return Response({'username': myusername}, status=status.HTTP_200_OK)

    def username_change(self, request):
        this_user = request.user
        my_username = ChangeUsernameSerializer(data=request.data, user=this_user)
        my_username.is_valid()
        old_username = my_username.validated_data["old_username"]
        new_username = my_username.validated_data["new_username"]

        if old_username != this_user.username:
            raise serializers.ValidationError('Wrong Username.')
        elif Tuser.objects.filter(username=new_username).count() > 0:
            raise serializers.ValidationError('This username is already in use.')
        elif old_username == new_username:
            raise serializers.ValidationError("Old username and new username can't be the same")
        else:
            this_user.username = new_username
            this_user.save()
            messages.success(request, 'Successfully Updated your username')
            Notification.objects.create(user=self.request.user, title='Username update',
                                        description='Username has been changed', type=0)
            return Response({'code': 1, 'response': 'Successfully changed username'})


class PhoneNumberUpdateView(viewsets.ViewSet):
    def get_phone_no(self, request):
        user = get_object_or_404(Tuser, id=request.user.id)
        mynumber = user.phone_number
        return Response({'phone_number': mynumber}, status=status.HTTP_200_OK)

    def phone_change(self, request):
        this_user = request.user
        my_number = ChangePhoneNumberSerializer(data=request.data, user=this_user)
        my_number.is_valid()
        old_phone_number = proper_dial(my_number.validated_data["old_phone_number"])
        new_phone_number = proper_dial(my_number.validated_data["new_phone_number"])

        if old_phone_number != this_user.phone_number:
            raise serializers.ValidationError('Wrong Phone_number.')
        elif Tuser.objects.filter(phone_number=new_phone_number).count() > 0:
            raise serializers.ValidationError('This Phone number is already in use.')
        elif old_phone_number == new_phone_number:
            raise serializers.ValidationError("Old number and new number can't be the same")
        else:
            this_user.phone_number = new_phone_number
            this_user.save()
            messages.success(request, 'Successfully Changed your Phone number')
            Notification.objects.create(user=self.request.user, title='Phone number updated',
                                        description='Phone number has been changed', type=0)
            return Response({'code': 1, 'response': 'Successfully changed Phone number'})


class ProfilePicViewSet(generics.RetrieveUpdateAPIView, mixins.UpdateModelMixin):
    queryset = Tuser.objects.all()
    serializer_class = ProfilePicSerializer

    def get_object(self):
        return self.request.user


class VerificationAPI(viewsets.ViewSet):
    authentication_classes = ()
    permission_classes = ()

    def verify_user(self, request):

        username = request.session['tusername']
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


class ChangePasswordAPI(APIView):

    def put(self, request):
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
            try:
                this_user = Tuser.objects.get(phone_number=proper_dial(mobile))
            except Tuser.DoesNotExist:
                this_user = None

            if this_user is not None:
                if Reset_password.objects.filter(user=this_user).exists():
                    x = Reset_password.objects.filter(user=this_user).update(reset_code=reset_code(),
                                                                        expiry=timezone.now() + expiry_date())
                else:
                    x = Reset_password.objects.create(user=this_user, reset_code=reset_code(),
                                                 expiry=timezone.now() + expiry_date())
                request.session['u_id'] = this_user.id
                sms.send("Reset password code: " + str(x.reset_code), [proper_dial(mobile)])
                messages.info(request, 'enter code sent to ' + this_user.mobile)
            return Response({'code': 1, 'response': password_rese.data}, status=status.HTTP_200_OK)
        return Response({'code': 0, 'response': password_rese.errors}, status=status.HTTP_400_BAD_REQUEST)


class ResetCode(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post_code(self, request):
        user_id = request.session['u_id']
        this_user = Tuser.objects.get(id=user_id)
        my_reset_code = get_object_or_404(Reset_password, user=this_user)
        code = EnterResetSerializer(data=request.data)

        if code.is_valid():
            reset_code = code.validated_data['reset_code']
            if my_reset_code.expiry > timezone.now():
                if reset_code == my_reset_code.reset_code:
                    return Response({'code': 1, 'response': code.data}, status=status.HTTP_200_OK)
        return Response({'code': 0, 'response': code.errors}, status=status.HTTP_400_BAD_REQUEST)


class PasswordReset(APIView):
    authentication_classes = ()
    permission_classes = ()

    def reset_pass(self, request):
        user_id = request.session['u_id']
        user = get_object_or_404(Tuser, id=user_id)
        pass_reset = RestePassword(data=request.data)
        if pass_reset.is_valid():
            new_password = pass_reset.validated_data['password']
            new_password_confirm = pass_reset.validated_data['confirm_password']
            if new_password == new_password_confirm:
                if len(new_password) > 8 and len(new_password_confirm) > 8:
                    user.set_password(new_password)
                    return Response({'code': 1, 'response': pass_reset.data}, status=status.HTTP_200_OK)
        return Response({'code': 0}, status=status.HTTP_400_BAD_REQUEST)


class ResendCode(viewsets.ViewSet):
    authentication_classes = ()
    permission_classes = ()

    def resend_code(self, request, username):
        this_user = Tuser.objects.get(username=username)
        Tuser.objects.filter(username=this_user.username).update(verification_code=generate_verification_code())
        sms.send("Tossapp Verification code: " + str(this_user.verification_code), [this_user.phone_number])
        return Response({'code': 1}, status=status.HTTP_200_OK)
