# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
import random

from django.db.models import F
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, serializers, generics, mixins
from rest_framework.response import Response
from daily_lotto.daily_l import todays_lotto, ticket_count
from daily_lotto.hourly_lotto import hourly_lotto
from daily_lotto.models import *
from daily_lotto.quaterly_lotto import quaterly_lotto
from daily_lotto.views import balance_calculator
from lotto_api.lotto_serializers import TicketDailySerializer, MultipleDailySerializer, AlltimeSerializer
from tossapp.models import *


lotto_game = Game.objects.get(name='Daily Lotto')
# lotto fee
fee = DailyLotto.TICKET_PRICE * DailyLotto.HOUSE_COMMISSION_RATE


class TicketDailyCreate(viewsets.ViewSet):

    def get(self, request):
        response = []
        today_lotto = {
            'bought_tickets': DailyLottoTicket.objects.filter(daily_lotto=todays_lotto()).count(),
        }
        response.append(today_lotto)
        return Response({'response': today_lotto}, status=status.HTTP_200_OK)

    def my_tickets(self, request):
        current_lotto = todays_lotto()
        ends = current_lotto.end_date

        my_daily_tickets = TicketDailySerializer(data=request.data)
        my_daily_tickets.is_valid(raise_exception=True)
        n1 = my_daily_tickets.validated_data["n1"]
        n2 = my_daily_tickets.validated_data["n2"]
        n3 = my_daily_tickets.validated_data["n3"]
        n4 = my_daily_tickets.validated_data["n4"]
        n5 = my_daily_tickets.validated_data["n5"]
        n6 = my_daily_tickets.validated_data["n6"]
        ticket_cost = DailyLotto.TICKET_PRICE

        if timezone.now() < ends:
            if ticket_cost < self.request.user.balance:

                DailyLottoTicket.objects.create(daily_lotto=todays_lotto(), player_name=self.request.user, n1=n1, n2=n2, n3=n3,
                                                n4=n4, n5=n5, n6=n6)

                # calculating users balance
                new_balance = balance_calculator(request.user.balance, ticket_cost)
                Tuser.objects.filter(username=self.request.user.username).update(balance=new_balance)
                Game_stat.objects.create(user=self.request.user, game=lotto_game, bet_amount=ticket_cost, status=Game_stat.PENDING,
                                         service_fee=fee)
                Game.objects.filter(name='Daily Lotto').update(times_played=F("times_played") + 1)
            else:
                raise serializers.ValidationError("Insufficient balance")
        else:
            raise serializers.ValidationError("Time has ended. Next lotto starts at midnight")

        return Response({'code': 1, 'response': 'Successfully bought'})


class MultipleDailyTicket(viewsets.ViewSet):
    def get(self):
        response = []
        today_lotto = {
            'bought_tickets': DailyLottoTicket.objects.filter(daily_lotto=todays_lotto()).count(),
        }
        response.append(today_lotto)
        return Response({'response': today_lotto}, status=status.HTTP_200_OK)

    def other_tickets(self, request):
        current_lotto = todays_lotto()
        ends = current_lotto.end_date
        my_daily_tickets = MultipleDailySerializer(data=request.data)
        my_daily_tickets.is_valid(raise_exception=True)
        ticketno = my_daily_tickets.validated_data["quantity"]
        if ticketno is None:
            ticketno = 0
        else:
            ticketno = my_daily_tickets.validated_data["quantity"]
        ticket_cost = ticketno * DailyLotto.TICKET_PRICE  # total cost of random tickets

        if timezone.now() < ends:
            if ticket_cost < self.request.user.balance:
                if ticketno > 0:
                    for random_qunatity in range(ticketno):
                        generated_numbers = random.sample(range(1, 20), 6)
                        t1, t2, t3, t4, t5, t6 = generated_numbers
                        DailyLottoTicket.objects.create(player_name=self.request.user, daily_lotto=todays_lotto(),
                                                        n1=t1, n2=t2, n3=t3, n4=t4, n5=t5, n6=t6)
                    # calculating ticket cost
                    multiple_ticket_service_fee = fee * ticketno
                    # calculating users balance
                    new_balance = balance_calculator(request.user.balance, ticket_cost)
                    Tuser.objects.filter(username=self.request.user.username).update(balance=new_balance)
                    Game_stat.objects.create(user=self.request.user, game=lotto_game, bet_amount=ticket_cost,
                                             status=Game_stat.PENDING,
                                             service_fee=multiple_ticket_service_fee)
                    Game.objects.filter(name='Daily Lotto').update(times_played=F("times_played") + 1)
                else:
                    raise serializers.ValidationError("Ticket number should be greater than zero")
            else:
                raise serializers.ValidationError("Insufficient balance")
        else:
            raise serializers.ValidationError("Time has ended. Next lotto starts at midnight")

        return Response({'code': 1, 'response': 'Successfully bought'})


class AllTimeWinnersAPI(generics.ListAPIView, mixins.ListModelMixin):
    queryset = DailyLottoResult.objects.all().order_by('-prize')[:15]
    serializer_class = AlltimeSerializer


class PreviousLottoAPI(viewsets.ViewSet):

    def get_previous_lottos(self, request, lotto_date):
        response = []
        previous_daily_lotto = get_object_or_404(DailyLotto, start_date=lotto_date, lotto_type='D')

        details = {
            'draw_date': previous_daily_lotto.end_date,
            'win1': previous_daily_lotto.win1,
            'win2': previous_daily_lotto.win2,
            'win3': previous_daily_lotto.win3,
            'win4': previous_daily_lotto.win4,
            'win5': previous_daily_lotto.win5,
            'win6': previous_daily_lotto.win6,
            'jackpot': previous_daily_lotto.jack_pot,
            'number6Winners': DailyLottoTicket.objects.filter(daily_lotto=previous_daily_lotto, hits=6).count(),
            'number5Winners': DailyLottoTicket.objects.filter(daily_lotto=previous_daily_lotto, hits=5).count(),
            'number4Winners': DailyLottoTicket.objects.filter(daily_lotto=previous_daily_lotto, hits=4).count(),
            'number3Winners': DailyLottoTicket.objects.filter(daily_lotto=previous_daily_lotto, hits=3).count(),
        }
        response.append(details)
        return Response({'response': response, 'winners': AlltimeSerializer(DailyLottoResult.objects.filter
                                                                            (daily_lotto=previous_daily_lotto),
                                                                            many=True).data}, status=status.HTTP_200_OK)

"""
class TicketQuaterlyCreate(viewsets.ViewSet):

    def get(self):
        response = []
        today_lotto = {
            'bought_tickets': DailyLottoTicket.objects.filter(daily_lotto=quaterly_lotto()).count(),
        }
        response.append(today_lotto)
        return Response({'response': today_lotto}, status=status.HTTP_200_OK)

    def my_tickets(self, request):
        current_lotto = quaterly_lotto()
        ends = current_lotto.end_date

        my_daily_tickets = TicketDailySerializer(data=request.data)
        my_daily_tickets.is_valid(raise_exception=True)
        n1 = my_daily_tickets.validated_data["n1"]
        n2 = my_daily_tickets.validated_data["n2"]
        n3 = my_daily_tickets.validated_data["n3"]
        n4 = my_daily_tickets.validated_data["n4"]
        n5 = my_daily_tickets.validated_data["n5"]
        n6 = my_daily_tickets.validated_data["n6"]
        ticket_cost = DailyLotto.TICKET_PRICE

        if timezone.now() < ends:
            if ticket_cost < self.request.user.balance:

                DailyLottoTicket.objects.create(daily_lotto=quaterly_lotto(), player_name=self.request.user, n1=n1,
                                                n2=n2, n3=n3, n4=n4, n5=n5, n6=n6)

                # calculating users balance
                new_balance = balance_calculator(request.user.balance, ticket_cost)
                Tuser.objects.filter(username=self.request.user.username).update(balance=new_balance)
                Game_stat.objects.create(user=self.request.user, game=lotto_game, bet_amount=ticket_cost,
                                         status=Game_stat.PENDING, service_fee=fee)
                Game.objects.filter(name='Daily Lotto').update(times_played=F("times_played") + 1)
            else:
                raise serializers.ValidationError("Insufficient balance")
        else:
            raise serializers.ValidationError("Next lotto will start in 6 minutes time time")
        return Response({'code': 1, 'response': 'Successfully bought'})


class MultipleQuaterlyTicket(viewsets.ViewSet):
    def get(self):
        response = []
        today_lotto = {
            'bought_tickets': DailyLottoTicket.objects.filter(daily_lotto=quaterly_lotto()).count(),
        }
        response.append(today_lotto)
        return Response({'response': today_lotto}, status=status.HTTP_200_OK)

    def other_tickets(self, request):
        current_lotto = quaterly_lotto()
        ends = current_lotto.end_date
        my_daily_tickets = MultipleDailySerializer(data=request.data)
        my_daily_tickets.is_valid(raise_exception=True)
        ticketno = my_daily_tickets.validated_data["quantity"]
        if ticketno is None:
            ticketno = 0
        else:
            ticketno = my_daily_tickets.validated_data["quantity"]
        ticket_cost = ticketno * DailyLotto.TICKET_PRICE  # total cost of random tickets

        if timezone.now() < ends:
            if ticket_cost < self.request.user.balance:
                if ticketno > 0:
                    for random_qunatity in range(ticketno):
                        generated_numbers = random.sample(range(1, 20), 6)
                        t1, t2, t3, t4, t5, t6 = generated_numbers
                        DailyLottoTicket.objects.create(player_name=self.request.user, daily_lotto=quaterly_lotto(),
                                                        n1=t1, n2=t2, n3=t3, n4=t4, n5=t5, n6=t6)
                    # calculating ticket cost
                    multiple_ticket_service_fee = fee * ticketno
                    # calculating users balance
                    new_balance = balance_calculator(request.user.balance, ticket_cost)
                    Tuser.objects.filter(username=self.request.user.username).update(balance=new_balance)
                    Game_stat.objects.create(user=self.request.user, game=lotto_game, bet_amount=ticket_cost,
                                             status=Game_stat.PENDING,
                                             service_fee=multiple_ticket_service_fee)
                    Game.objects.filter(name='Daily Lotto').update(times_played=F("times_played") + 1)
                else:
                    raise serializers.ValidationError("Ticket number should be greater than zero")
            else:
                raise serializers.ValidationError("Insufficient balance")
        else:
            raise serializers.ValidationError("Time has ended. Next lotto starts in 5 minutes time")

        return Response({'code': 1, 'response': 'Successfully bought'})


class TicketHourlyCreate(viewsets.ViewSet):

    def get(self):
        response = []
        today_lotto = {
            'bought_tickets': DailyLottoTicket.objects.filter(daily_lotto=hourly_lotto()).count(),
        }
        response.append(today_lotto)
        return Response({'response': today_lotto}, status=status.HTTP_200_OK)

    def my_tickets(self, request):
        current_lotto = hourly_lotto()
        ends = current_lotto.end_date

        my_daily_tickets = TicketDailySerializer(data=request.data)
        my_daily_tickets.is_valid(raise_exception=True)
        n1 = my_daily_tickets.validated_data["n1"]
        n2 = my_daily_tickets.validated_data["n2"]
        n3 = my_daily_tickets.validated_data["n3"]
        n4 = my_daily_tickets.validated_data["n4"]
        n5 = my_daily_tickets.validated_data["n5"]
        n6 = my_daily_tickets.validated_data["n6"]
        ticket_cost = DailyLotto.TICKET_PRICE

        if timezone.now() < ends:
            if ticket_cost < self.request.user.balance:

                DailyLottoTicket.objects.create(daily_lotto=hourly_lotto(), player_name=self.request.user, n1=n1,
                                                n2=n2, n3=n3, n4=n4, n5=n5, n6=n6)

                # calculating users balance
                new_balance = balance_calculator(request.user.balance, ticket_cost)
                Tuser.objects.filter(username=self.request.user.username).update(balance=new_balance)
                Game_stat.objects.create(user=self.request.user, game=lotto_game, bet_amount=ticket_cost,
                                         status=Game_stat.PENDING, service_fee=fee)
                Game.objects.filter(name='Daily Lotto').update(times_played=F("times_played") + 1)
            else:
                raise serializers.ValidationError("Insufficient balance")
        else:
            raise serializers.ValidationError("Next lotto will start in 6 minutes time time")
        return Response({'code': 1, 'response': 'Successfully bought'})



class MultipleHourlyTicket(viewsets.ViewSet):
    def get(self):
        response = []
        today_lotto = {
            'bought_tickets': DailyLottoTicket.objects.filter(daily_lotto=hourly_lotto()).count(),
        }
        response.append(today_lotto)
        return Response({'response': today_lotto}, status=status.HTTP_200_OK)

    def other_tickets(self, request):
        current_lotto = hourly_lotto()
        ends = current_lotto.end_date
        my_daily_tickets = MultipleDailySerializer(data=request.data)
        my_daily_tickets.is_valid(raise_exception=True)
        ticketno = my_daily_tickets.validated_data["quantity"]
        if ticketno is None:
            ticketno = 0
        else:
            ticketno = my_daily_tickets.validated_data["quantity"]
        ticket_cost = ticketno * DailyLotto.TICKET_PRICE  # total cost of random tickets

        if timezone.now() < ends:
            if ticket_cost < self.request.user.balance:
                if ticketno > 0:
                    for random_qunatity in range(ticketno):
                        generated_numbers = random.sample(range(1, 20), 6)
                        t1, t2, t3, t4, t5, t6 = generated_numbers
                        DailyLottoTicket.objects.create(player_name=self.request.user, daily_lotto=hourly_lotto(),
                                                        n1=t1, n2=t2, n3=t3, n4=t4, n5=t5, n6=t6)
                    # calculating ticket cost
                    multiple_ticket_service_fee = fee * ticketno
                    # calculating users balance
                    new_balance = balance_calculator(request.user.balance, ticket_cost)
                    Tuser.objects.filter(username=self.request.user.username).update(balance=new_balance)
                    Game_stat.objects.create(user=self.request.user, game=lotto_game, bet_amount=ticket_cost,
                                             status=Game_stat.PENDING,
                                             service_fee=multiple_ticket_service_fee)
                    Game.objects.filter(name='Daily Lotto').update(times_played=F("times_played") + 1)
                else:
                    raise serializers.ValidationError("Ticket number should be greater than zero")
            else:
                raise serializers.ValidationError("Insufficient balance")
        else:
            raise serializers.ValidationError("Time has ended. Next lotto starts in 5 minutes time")

        return Response({'code': 1, 'response': 'Successfully bought'})
        """

