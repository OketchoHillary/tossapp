# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from daily_lotto.models import DailyLottoTicket
from lotto_api.lotto_serializers import SingleTicketSerializer


class SingleTicketCreate(generics.CreateAPIView):
    queryset = DailyLottoTicket.objects.all()
    serializer_class = SingleTicketSerializer
