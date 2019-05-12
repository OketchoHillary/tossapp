from rest_framework import serializers
from tossapp.models import *


class NotificationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = '__all__'


class GamesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        exclude = ['id']


class GamesHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Game_stat
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'


class WithdrawSerializer(serializers.Serializer):
    amount = serializers.CharField()


class DepositSerializer(serializers.Serializer):
    amount = serializers.IntegerField()

