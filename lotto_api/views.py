# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
import random

from django.db.models import F
from rest_framework import viewsets, status
from rest_framework.response import Response

from accounts.models import Tuser
from daily_lotto.lotto_components import todays_lotto, ticket_count
from daily_lotto.models import DailyLottoTicket, DailyLotto
from daily_lotto.views import balance_calculator
from lotto_api.lotto_serializers import TicketDailySerializer, MultipleDailySerializer
from tossapp.models import Game_stat, Game


lotto_game = Game.objects.get(name='Daily Lotto')
# lotto fee
fee = DailyLotto.TICKET_PRICE * DailyLotto.HOUSE_COMMISSION_RATE


class TicketDailyCreate(viewsets.ViewSet):

    def get(self, request):
        response = []
        bought_tickets = ticket_count
        today_lotto = {
            'bought_tickets': DailyLottoTicket.objects.filter(daily_lotto=todays_lotto()).count(),
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

        DailyLottoTicket.objects.create(daily_lotto=todays_lotto(), player_name=self.request.user, n1=n1, n2=n2, n3=n3,
                                        n4=n4, n5=n5, n6=n6)

        ticket_cost = DailyLotto.TICKET_PRICE
        # calculating users balance
        new_balance = balance_calculator(request.user.balance, ticket_cost)
        Tuser.objects.filter(username=self.request.user.username).update(balance=new_balance)
        Game_stat.objects.create(user=self.request.user, game=lotto_game, bet_amount=ticket_cost, status=Game_stat.PENDING,
                                 service_fee=fee)
        Game.objects.filter(name='Daily Lotto').update(times_played=F("times_played") + 1)
        return Response({'code': 1, 'response': 'Successfully bought'})


class MultipleDailyTicket(viewsets.ViewSet):
    def get(self, request):
        response = []
        bought_tickets = ticket_count
        today_lotto = {
            'bought_tickets': bought_tickets,
        }
        response.append(today_lotto)
        return Response({'response': today_lotto}, status=status.HTTP_200_OK)

    def other_tickets(self, request):
        my_daily_tickets = MultipleDailySerializer(data=request.data)
        my_daily_tickets.is_valid(raise_exception=True)
        ticketno = my_daily_tickets.validated_data["quantity"]
        if ticketno is None:
            ticketno = 0
        else:
            ticketno = my_daily_tickets.validated_data["quantity"]

        if ticketno > 0:
            for random_qunatity in range(ticketno):
                generated_numbers = random.sample(range(1, 20), 6)
                t1, t2, t3, t4, t5, t6 = generated_numbers
                DailyLottoTicket.objects.create(player_name=self.request.user, daily_lotto=todays_lotto(), n1=t1, n2=t2, n3=t3,
                                                n4=t4, n5=t5, n6=t6)
        # calculating ticket cost
        ticket_cost = ticketno * DailyLotto.TICKET_PRICE  # total cost of random tickets
        multiple_ticket_service_fee = fee * ticketno
        # calculating users balance
        new_balance = balance_calculator(request.user.balance, ticket_cost)
        Tuser.objects.filter(username=self.request.user.username).update(balance=new_balance)
        Game_stat.objects.create(user=self.request.user, game=lotto_game, bet_amount=ticket_cost,
                                 status=Game_stat.PENDING,
                                 service_fee=multiple_ticket_service_fee)
        Game.objects.filter(name='Daily Lotto').update(times_played=F("times_played") + 1)
        return Response({'code': 1, 'response': 'Successfully bought'})

