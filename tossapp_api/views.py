# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Count
from rest_framework import status

from tossapp_api.tossapp_serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response


class NotificationView(APIView):
    def get(self, request, username):
        return Response(NotificationsSerializer(Notification.objects.filter(user__username=username), many=True).data)


class GameAPIView(APIView):
    def get(self, request):
        return Response(GamesSerializer(Game.objects.all(), many=True).data)


class ReferralAPI(APIView):

    def get(self, request, username):
        response = []
        user = Tuser.objects.get(username=username)
        t_user_count = Tuser.objects.filter(referrer=user).count()
        players = Tuser.objects.all().annotate(num_refferals=Count('referrals')).order_by('-num_refferals')[:10]
        ref_details = {
            'rank': user.refferal_ranking,
            'count': t_user_count,
            'points': user.points,
            'ref_prize': user.referrer_prize,
        }
        response.append(ref_details)
        return Response({'response': response}, status=status.HTTP_200_OK)


class GameStatView(APIView):
    def get(self, request, username):
        return Response(GamesHistorySerializer(Game_stat.objects.filter(user__username=username), many=True).data)


class TransactionView(APIView):
    def get(self, request, username):
        return Response(TransactionSerializer(Transaction.objects.filter(user__username=username), many=True).data)


