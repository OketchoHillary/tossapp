# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
import random

from rest_framework import generics, viewsets, status
from rest_framework.response import Response

from daily_lotto.lotto_components import todays_lotto, ticket_count
from daily_lotto.models import DailyLottoTicket
from lotto_api.lotto_serializers import SingleTicketDailySerializer, MultipleTicketSerializer


class SingleTicketDailyCreate(viewsets.ViewSet):
    def get(self, request):
        response = []
        bought_tickets = ticket_count
        today_lotto = {
            'bought_tickets': bought_tickets,
        }
        response.append(today_lotto)
        return Response({'response': response}, status=status.HTTP_200_OK)

    # Single ticket
    def single_ticket(self, request):
        new_daily_ticket = SingleTicketDailySerializer(data=request.data)
        if new_daily_ticket.is_valid():
            new_daily_ticket.save()
            return Response({'code': 1, 'response': new_daily_ticket.data}, status=status.HTTP_201_CREATED)
        return Response({'code': 0, 'response': new_daily_ticket.errors}, status=status.HTTP_400_BAD_REQUEST)

    # Random tickets
    def multiple_ticket(self, request):
        multi_daily_ticket = MultipleTicketSerializer(data=request.data)
        multi_daily_ticket.is_valid(raise_exception=True)
        ticketno = multi_daily_ticket.validated_data["quantity"]
        if ticketno is None:
            ticketno = 0
        else:
            ticketno = multi_daily_ticket.validated_data["quantity"]
        if ticketno > 1:
            for random_qunatity in range(ticketno):
                generated_numbers = random.sample(range(1, 20), 6)
                t1, t2, t3, t4, t5, t6 = generated_numbers
                DailyLottoTicket.objects.create(player_name=self.request.user, daily_lotto=todays_lotto(), n1=t1, n2=t2, n3=t3,
                                                n4=t4, n5=t5, n6=t6)
        return Response({'code': 0, 'response': ticketno}, status=status.HTTP_400_BAD_REQUEST)


