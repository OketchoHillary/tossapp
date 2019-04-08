# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import (login, logout)
from rest_framework import generics, permissions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

# Account APIs
from api.account_serializers import *
from daily_lotto.models import DailyLottoTicket
from lotto_api.lotto_serializers import SingleTicketSerializer


# Create your views here.


class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer


class LoginView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token':token.key}, status=200)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        logout(request)
        return Response(status=204)

"""
class ProfileView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserProfileSerializer

    def get_object(self):
        username = self.kwargs["username"]
        obj = get_object_or_404(Tuser, username=username)
        return obj
        """


class ProfileView(viewsets.ViewSet):
    def get_profile(self, username):
        try:
            userprofile = Tuser.objects.get(username=username)
            return userprofile
        except Tuser.DoesNotExist as e:
            return False

    def get_this_profile(self, request, username):
        queryset = self.get_profile(username)
        if queryset:
            profile = UserProfileSerializer(queryset)
            return Response({'code': 1, 'response': profile.data})
        else:
            return Response({'message': "Does Not Exist", 'code': 0})

    def update_profile(self, request, username):
        profile_instance = self.get_profile(username)
        if profile_instance:
            updated_profile = UserProfileSerializer(profile_instance, data=request.data)
            if updated_profile.is_valid():
                updated_profile.save()
                return Response({'code': 1, 'response': updated_profile.data})
            return Response({'code': 0, 'response': updated_profile.errors}, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({'code': 0})