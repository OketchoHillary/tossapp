# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
import random

from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from api.permissions import IsOwnerOrReadOnly
from daily_lotto.lotto_components import todays_lotto, ticket_count
from daily_lotto.models import DailyLottoTicket
from lotto_api.lotto_serializers import TicketDailySerializer
from tossapp.models import Game_stat


class TicketDailyCreate(viewsets.ViewSet):

    def get(self, request):
        response = []
        bought_tickets = ticket_count
        today_lotto = {
            'bought_tickets': bought_tickets,
        }
        response.append(today_lotto)
        return Response({'response': today_lotto}, status=status.HTTP_200_OK)

    def my_tickets(self, request):
        my_daily_tickets = TicketDailySerializer(data=request.data)
        my_daily_tickets.is_valid(raise_exception=True)
        n1 = my_daily_tickets.validated_data["n1"]
        n2 = my_daily_tickets.validated_data["n2"]
        n3 = my_daily_tickets.validated_data["n3"]
        n4 = my_daily_tickets.validated_data["n4"]
        n5 = my_daily_tickets.validated_data["n5"]
        n6 = my_daily_tickets.validated_data["n6"]
        ticketno = my_daily_tickets.validated_data["quantity"]
        if ticketno is None:
            ticketno = 0
        else:
            ticketno = my_daily_tickets.validated_data["quantity"]
        DailyLottoTicket.objects.create(daily_lotto=todays_lotto(), player_name=self.request.user, n1=n1, n2=n2, n3=n3,
                                        n4=n4, n5=n5, n6=n6)
        if ticketno > 0:
            for random_qunatity in range(ticketno):
                generated_numbers = random.sample(range(1, 20), 6)
                t1, t2, t3, t4, t5, t6 = generated_numbers
                DailyLottoTicket.objects.create(player_name=self.request.user, daily_lotto=todays_lotto(), n1=t1, n2=t2, n3=t3,
                                                n4=t4, n5=t5, n6=t6)
                """
        Game_stat.objects.create(user=request.user, game=lotto_game, bet_amount=total_bet, status=Game_stat.PENDING,
                                 service_fee=service_fee)
                                 """

        return Response({'code': 0, 'response': ticketno}, status=status.HTTP_400_BAD_REQUEST)


