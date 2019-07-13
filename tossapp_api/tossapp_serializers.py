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

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(WithdrawSerializer, self).__init__(*args, **kwargs)

    amount = serializers.IntegerField()
    password = serializers.CharField()


class DepositSerializer(serializers.Serializer):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(DepositSerializer, self).__init__(*args, **kwargs)

    amount = serializers.IntegerField()
    password = serializers.CharField()

