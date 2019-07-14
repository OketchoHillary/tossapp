# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
from django.contrib.auth.hashers import check_password
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
        return Response({'response': response, 'players': players}, status=status.HTTP_200_OK)


class GameStatView(APIView):
    def get(self, request):
        return Response(GamesHistorySerializer(Game_stat.objects.filter(user=request.user), many=True).data)


class TransactionHistoryView(APIView):
    def get(self, request):
        return Response(TransactionSerializer(Transaction.objects.filter(user=request.user), many=True).data)


class TransactionView(viewsets.ViewSet):
    def get(self, request):
        response = []
        bal = {
            'balance': request.user.balance,
        }

        response.append(bal)

        return Response({'response': bal}, status=status.HTTP_200_OK)

    def fund_deposit(self, request):
        depo = DepositSerializer(data=request.data, user=request.user)
        if depo.is_valid():
            amount = depo.validated_data["amount"]
            password = depo.validated_data["password"]
            payload = {'command': 'jpesa', 'action': 'deposit', 'username': 'emmanuel.m', 'password': 'yoonek17',
                       'IS_GET': 3, 'number': request.user.phone_number, 'amount': amount}
            url = "https://secure.jpesa.com/api.php"
            valid_password = check_password(password, request.user.password)
            if valid_password:
                if 1000 <= amount <= 10000:
                    requests.post(url, data=payload)
                    print(requests.post(url, data=payload))
                    Transaction.objects.create(user=request.user, transaction_type=0, status=1, payment_method=0,
                                               amount=amount)
                    Tuser.objects.filter(id=request.user.id).update(balance=F("balance") + amount)
                else:
                    raise serializers.ValidationError("Deposits should range between 1000 to 10000")
            else:
                raise serializers.ValidationError("wrong password")
        return Response(status=status.HTTP_202_ACCEPTED)

    def fund_withdraw(self, request):
        withdraw = WithdrawSerializer(data=request.data, user=request.user)
        if withdraw.is_valid():
            amount = withdraw.validated_data["amount"]
            password = withdraw.validated_data["password"]
            payload = {'dad': 'xpress', 'business':'emupuya@gmail.com', 'item_name':'Donations', 'amount':amount,
                       'currency_code':'UGX', 'return':'http://www.jolis.net', 'cancel': 'http://www.jolis.net'}
            url = "https://secure.jpesa.com"
            valid_password = check_password(password, request.user.password)
            if valid_password:
                if 1000 <= amount <= 10000:
                    requests.post(url, data=payload)
                    Transaction.objects.create(user=request.user, transaction_type=1, status=1, payment_method=0,
                                               amount=amount)
                    Tuser.objects.filter(id=request.user.id).update(balance=F("balance") - amount)

                else:
                    raise serializers.ValidationError("Withdrawals should range between 1000 to 10000")
            else:
                raise serializers.ValidationError("wrong password")
        return Response(status=status.HTTP_202_ACCEPTED)




