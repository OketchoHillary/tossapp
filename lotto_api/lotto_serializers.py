from django.db.models import F
from rest_framework import serializers, exceptions

from daily_lotto.models import *
from daily_lotto.views import todays_lotto
from tossapp.models import Game


class SingleTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyLottoTicket
        fields = ('player_name', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6')

    def create(self, validated_data):
        ticket = DailyLottoTicket(
            player_name=validated_data['player_name'],
            n1=validated_data['n1'],
            n2=validated_data['n2'],
            n3=validated_data['n3'],
            n4=validated_data['n4'],
            n5=validated_data['n5'],
            n6=validated_data['n6'],
        )
        ticket.daily_lotto = todays_lotto()
        ticket.save()
        Game.objects.filter(name='Daily Lotto').update(times_played=F("times_played") + 1)

        return ticket
