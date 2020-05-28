from __future__ import unicode_literals
import requests
from django.contrib.auth.hashers import check_password
from django.db.models import Count, F
from rest_framework import status, serializers
from rest_framework.pagination import PageNumberPagination

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response

# info for jpesa
from accounts_api.models import Tuser
from tossapp_api.models import Notification, Game, Game_stat, Transaction
from tossapp_api.tossapp_serializers import NotificationsSerializer, GamesSerializer, PlayerSerializer, \
    GamesHistorySerializer, TransactionSerializer, DepositSerializer, WithdrawSerializer

payload2 = {'command': 'jpesa', 'action': 'info', 'username': 'emmanuel.m', 'password': 'yoonek17',
                        'IS_GET': 3, 'tid': '7254D08FF0FA62E20E26681485A71568'}

class NotificationView(viewsets.ModelViewSet):
    pagination_class = PageNumberPagination
    queryset = Notification.objects.all()
    serializer_class = NotificationsSerializer

    def list_not(self, request):
        return Response(NotificationsSerializer(Notification.objects.filter(user=self.request.user), many=True).data)


class GameAPIView(APIView):
    def get(self, request):
        return Response(GamesSerializer(Game.objects.all(), many=True).data)


class ReferralAPI(APIView):

    def get(self, request):

        my_referrals = Tuser.objects.filter(referrer=request.user).annotate(num_refferals=Count('referrals')).order_by('-num_refferals')
        players = Tuser.objects.all().annotate(num_refferals=Count('referrals')).order_by('-num_refferals')[:10]

        ref_details = {
            'share_code': request.user.share_code,
            'rank': request.user.refferal_ranking,
            'count': my_referrals.count(),
            'ref_prize': request.user.referrer_prize,
        }

        return Response({'response': ref_details, 'players': PlayerSerializer(players, many=True).data,
                         'my_refs': PlayerSerializer(my_referrals, many=True).data}, status=status.HTTP_200_OK)


class GameStatView(APIView):

    def get(self, request):
        return Response(GamesHistorySerializer(Game_stat.objects.filter(user=request.user), many=True).data)


class TransactionHistoryView(APIView):
    def get(self, request):
        return Response(TransactionSerializer(Transaction.objects.filter(user=request.user), many=True).data)


class TransactionView(viewsets.ViewSet):
    def get(self, request):

        info = {
            'phone_number': request.user.phone_number,
            'balance': request.user.balance,
        }

        return Response({'response': info}, status=status.HTTP_200_OK)

    def fund_deposit(self, request):
        depo = DepositSerializer(data=request.data, user=request.user)
        if depo.is_valid():
            amount = depo.validated_data["amount"]

            # jpesa url
            url = "https://secure.jpesa.com/api.php"
            payload = {'command': 'jpesa', 'action': 'deposit', 'username': 'emmanuel.m', 'password': 'yoonek17',
                       'IS_GET': 3, 'number': request.user.phone_number, 'amount': amount}

            if 1000 <= amount <= 10000:
                requests.post(url, data=payload)
                print('enter pin')
                info = requests.post(url, data=payload2)
                print(info.text)
                # Transaction.objects.create(user=request.user, transaction_type=0, status=1, payment_method=0,
                #                            amount=amount)
                # Tuser.objects.filter(id=request.user.id).update(balance=F("balance") + amount)

            else:
                raise serializers.ValidationError({'response':"Deposits should range between 1000 to 10000"})

        return Response({'response': 'Successfully deposited'}, status=status.HTTP_200_OK)

    def fund_withdraw(self, request):
        withdraw = WithdrawSerializer(data=request.data, user=request.user)
        if withdraw.is_valid():
            amount = withdraw.validated_data["amount"]
            password = withdraw.validated_data["password"]
            url = "https://secure.jpesa.com/api.php"
            payload = {'command': 'jpesa', 'action': 'withdraw', 'username': 'emmanuel.m', 'password': 'yoonek17',
                       'IS_GET': 3, 'number': request.user.phone_number, 'amount': amount}
            valid_password = check_password(password, request.user.password)
            if valid_password:
                if 1000 <= amount <= 10000:
                    received = requests.post(url, data=payload)
                    # Transaction.objects.create(user=request.user, transaction_type=0, status=1, payment_method=0,
                    #                            amount=amount)
                    # Tuser.objects.filter(id=request.user.id).update(balance=F("balance") - amount)

                else:
                    raise serializers.ValidationError({'response':"Withdrawals should range between 2000 to 10000"})
            else:
                raise serializers.ValidationError({'response':"wrong password"})
        return Response({'response': 'Successfully withdrawn'}, status=status.HTTP_202_ACCEPTED)

