from django.db.models import F
from rest_framework import serializers, exceptions
from tossapp.models import Game


class TicketDailySerializer(serializers.Serializer):
    n1 = serializers.IntegerField()
    n2 = serializers.IntegerField()
    n3 = serializers.IntegerField()
    n4 = serializers.IntegerField()
    n5 = serializers.IntegerField()
    n6 = serializers.IntegerField()
    quantity = serializers.IntegerField(required=False)

