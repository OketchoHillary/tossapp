"""
from rest_framework import serializers
from daily_lotto.models import *


class TicketDailySerializer(serializers.Serializer):
    n1 = serializers.IntegerField()
    n2 = serializers.IntegerField()
    n3 = serializers.IntegerField()
    n4 = serializers.IntegerField()
    n5 = serializers.IntegerField()
    n6 = serializers.IntegerField()


class MultipleDailySerializer(serializers.Serializer):
    quantity = serializers.IntegerField()


class AlltimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = DailyLottoResult
        exclude = ['id']
"""