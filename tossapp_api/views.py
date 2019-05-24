# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Count, F
from rest_framework import status
from tossapp_api.tossapp_serializers import *
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response


class NotificationView(APIView):

    def get(self, request):
        return Response(NotificationsSerializer(Notification.objects.filter(user=request.user), many=True).data)


class GameAPIView(APIView):
    def get(self, request):
        return Response(GamesSerializer(Game.objects.all(), many=True).data)


class ReferralAPI(APIView):

    def get(self, request):
        response = []
        t_user_count = Tuser.objects.filter(referrer=request.user).count()
        players = Tuser.objects.all().annotate(num_refferals=Count('referrals')).order_by('-num_refferals')[:10]
        ref_details = {
            'rank': request.user.refferal_ranking,
            'count': t_user_count,
            'points': request.user.points,
            'ref_prize': request.user.referrer_prize,
        }
        response.append(ref_details)
        return Response({'response': response}, status=status.HTTP_200_OK)


class GameStatView(APIView):
    def get(self, request):
        return Response(GamesHistorySerializer(Game_stat.objects.filter(user=request.user), many=True).data)


class TransactionHistoryView(APIView):
    def get(self, request):
        return Response(TransactionSerializer(Transaction.objects.filter(user=request.user), many=True).data)


class TransactionView(viewsets.ViewSet):
    def get(self, request):
        response = []
        my_balance = Tuser.objects.filter(id=request.user.id).values_list('balance')[0]
        balance = int(my_balance[0])
        bal = {
            'balance': balance,
        }

        response.append(bal)

        return Response({'response': bal}, status=status.HTTP_200_OK)

    def fund_deposit(self, request):
        depo = DepositSerializer(request.user)
        if depo.is_valid():
            amount = depo.validated_data["amount"]
            if amount > 999:
                Transaction.objects.create(user=request.user, transaction_type=0, status=1, payment_method=0,
                                           amount=amount)
                Tuser.objects.filter(id=request.user.id).update(balance=F("balance") + amount)
            else:
                raise serializers.ValidationError("Cant deposit less than 999 shillings")
        return Response(status=status.HTTP_202_ACCEPTED)

    def fund_withdraw(self, request):
        depo = WithdrawSerializer(request.user)
        if depo.is_valid():
            amount = depo.validated_data["amount"]
            if amount > 999:
                Transaction.objects.create(user=request.user, transaction_type=1, status=1, payment_method=0,
                                           amount=amount)
                Tuser.objects.filter(id=request.user.id).update(balance=F("balance") - amount)
            else:
                raise serializers.ValidationError("Cant withdraw less than 999 shillings")
        return Response(status=status.HTTP_202_ACCEPTED)




