from django.db.models import F
from rest_framework import serializers, exceptions

from daily_lotto.lotto_components import todays_lotto
from daily_lotto.models import *
from tossapp.models import Game


class TicketDailySerializer(serializers.Serializer):
    n1 = serializers.IntegerField()
    n2 = serializers.IntegerField()
    n3 = serializers.IntegerField()
    n4 = serializers.IntegerField()
    n5 = serializers.IntegerField()
    n6 = serializers.IntegerField()
    quantity = serializers.IntegerField(required=False)


class MultipleTicketSerializer(serializers.Serializer):
    quantity = serializers.IntegerField(required=False)

    def validate(self, data):
        quantity = data.get("quantity", "")

        if quantity > 0:
            Game.objects.filter(name='Daily Lotto').update(times_played=F("times_played") + 1)

        return data
