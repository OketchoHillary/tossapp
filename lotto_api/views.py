
from __future__ import unicode_literals

# Create your views here.
import datetime
import dateutil.parser as parser
import random
from django.db.models import F
from django.utils import timezone
from next_prev import next_in_order, prev_in_order
from rest_framework import status, serializers, generics, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from lotto_api.models import DailyLotto, DailyLottoTicket, DailyLottoResult
from lotto_api.lotto_serializers import TicketDailySerializer, MultipleDailySerializer, AlltimeSerializer
from tauth.task import create_random_tickets
from tossapp.models import *
from tossapp_api.models import Game, Game_stat
from tossapp_api.tossapp_serializers import GamesHistorySerializer


try:
    lotto_game = Game.objects.get(name='Daily Lotto')
except Game.DoesNotExist:
    lotto_game = 'Daily Lotto'

fee = DailyLotto.TICKET_PRICE * DailyLotto.HOUSE_COMMISSION_RATE


def total(single_form, multiple_tickets_form):
    return single_form + multiple_tickets_form


def hours_minutes_seconds(td):
    return td.seconds//3600, (td.seconds//60) % 60, td.seconds % 60


def convert_timedelta(duration):
    days, seconds = duration.days, duration.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    return '{}:{}:{}'.format(hours, minutes, seconds)


def balance_calculator(lar, ry):
    return lar - ry


def random_tickets(tick, req):
    latest_daily = DailyLotto.objects.filter(lotto_type='D')[0]
    my_quantity = tick.cleaned_data
    quantity = my_quantity.get('quantity')

    if quantity >= 1:
        for random_qunatity in range(quantity):
            generated_numbers = random.sample(range(1, 21), 6)
            t1,t2,t3,t4,t5,t6 = generated_numbers
            DailyLottoTicket.objects.create(player_name=req.user, daily_lotto=latest_daily, n1=t1, n2=t2, n3=t3,
                                            n4=t4, n5=t5, n6=t6)


class TicketDailyCreate(APIView):
    def get(self, request):
        latest_daily = DailyLotto.objects.filter(lotto_type='D')[0]
        previous_daily = DailyLotto.objects.filter(lotto_type='D')[1].jack_pot
        tickets = DailyLottoTicket.objects.filter(daily_lotto=latest_daily).count()
        daily_revenue = DailyLotto.TICKET_PRICE * tickets
        six_prize = DailyLotto.JACKPOT_SHARE_RATE * daily_revenue
        # getting difference in time delta
        x = latest_daily.end_date - timezone.now()
        ender = latest_daily.end_date
        dato = parser.parse(str(ender))
        current_time = datetime.datetime.now()

        today_lotto = {
            'bought_tickets': tickets,
            'end_date':dato.isoformat(),
            'current_time': current_time.isoformat(),
            'count_down': convert_timedelta(x),
            'jackpot': previous_daily + six_prize
        }

        return Response({'response': today_lotto}, status=status.HTTP_200_OK)

    def post(self, request):
        latest_daily = DailyLotto.objects.filter(lotto_type='D')[0]

        ends = latest_daily.end_date

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

                DailyLottoTicket.objects.create(daily_lotto=latest_daily, player_name=self.request.user, n1=n1, n2=n2, n3=n3,
                                                n4=n4, n5=n5, n6=n6)
                # calculating users balance
                new_balance = balance_calculator(request.user.balance, ticket_cost)
                Tuser.objects.filter(username=self.request.user.username).update(balance=new_balance)
                Game_stat.objects.create(user=self.request.user, game=lotto_game, bet_amount=ticket_cost,
                                         status=Game_stat.PENDING, service_fee=fee)
                Game.objects.filter(name='Daily Lotto').update(times_played=F("times_played") + 1)
            else:
                raise serializers.ValidationError({'response':"Insufficient balance"})
        else:
            raise serializers.ValidationError({'response':"Time has ended. Next lotto starts at midnight"})

        return Response({'code': 1, 'response': 'Successfully bought'})


class MultipleDailyTicket(APIView):

    def get(self, request):
        latest_daily = DailyLotto.objects.filter(lotto_type='D')[0]
        previous_daily = DailyLotto.objects.filter(lotto_type='D')[1].jack_pot
        tickets = DailyLottoTicket.objects.filter(daily_lotto=latest_daily).count()
        daily_revenue = DailyLotto.TICKET_PRICE * tickets
        six_prize = DailyLotto.JACKPOT_SHARE_RATE * daily_revenue
        # getting difference in time delta
        x = latest_daily.end_date - timezone.now()
        ender = latest_daily.end_date
        dato = parser.parse(str(ender))
        current_time = datetime.datetime.now()

        today_lotto = {
            'bought_tickets': tickets,
            'end_date': dato.isoformat(),
            'current_time': current_time.isoformat(),
            'count_down': convert_timedelta(x),
            'jackpot': previous_daily + six_prize
        }

        return Response({'response': today_lotto}, status=status.HTTP_200_OK)

    def post(self, request):
        latest_daily = DailyLotto.objects.filter(lotto_type='D')[0]
        ends = latest_daily.end_date
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
                    create_random_tickets.delay(ticketno, latest_daily.lotto_id, self.request.user.id)
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


class TicketQuaterlyCreate(APIView):

    def get(self, request):
        latest_quaterly = DailyLotto.objects.filter(lotto_type='Q')[0]
        previous_daily = DailyLotto.objects.filter(lotto_type='Q')[1].jack_pot
        tickets = DailyLottoTicket.objects.filter(daily_lotto=latest_quaterly).count()
        daily_revenue = DailyLotto.TICKET_PRICE * tickets
        six_prize = DailyLotto.JACKPOT_SHARE_RATE * daily_revenue
        # getting difference in time delta
        x = latest_quaterly.end_date - timezone.now()
        ender = latest_quaterly.end_date
        dato = parser.parse(str(ender))
        current_time = datetime.datetime.now()

        today_lotto = {
            'bought_tickets': tickets,
            'end_date': dato.isoformat(),
            'current_time': current_time.isoformat(),
            'count_down': convert_timedelta(x),
            'jackpot': previous_daily + six_prize
        }

        return Response({'response': today_lotto}, status=status.HTTP_200_OK)

    def post(self, request):
        latest_quaterly = DailyLotto.objects.filter(lotto_type='Q')[0]

        ends = latest_quaterly.end_date

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

                DailyLottoTicket.objects.create(daily_lotto=latest_quaterly, player_name=self.request.user, n1=n1,
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


class MultipleQuaterlyTicket(APIView):
    def get(self, request):
        latest_quaterly = DailyLotto.objects.filter(lotto_type='Q')[0]
        previous_daily = DailyLotto.objects.filter(lotto_type='Q')[1].jack_pot
        tickets = DailyLottoTicket.objects.filter(daily_lotto=latest_quaterly).count()
        daily_revenue = DailyLotto.TICKET_PRICE * tickets
        six_prize = DailyLotto.JACKPOT_SHARE_RATE * daily_revenue
        # getting difference in time delta
        x = latest_quaterly.end_date - timezone.now()
        ender = latest_quaterly.end_date
        dato = parser.parse(str(ender))
        current_time = datetime.datetime.now()

        today_lotto = {
            'bought_tickets': tickets,
            'end_date': dato.isoformat(),
            'current_time': current_time.isoformat(),
            'count_down': convert_timedelta(x),
            'jackpot': previous_daily + six_prize
        }

        return Response({'response': today_lotto}, status=status.HTTP_200_OK)

    def post(self, request):
        latest_quaterly = DailyLotto.objects.filter(lotto_type='Q')[0]

        ends = latest_quaterly.end_date
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
                    create_random_tickets.delay(ticketno, latest_quaterly.lotto_id, self.request.user.id)
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


class TicketHourlyCreate(APIView):
    def get(self, request):

        latest_hourly = DailyLotto.objects.filter(lotto_type='H')[0]
        previous_daily = DailyLotto.objects.filter(lotto_type='H')[1].jack_pot
        tickets = DailyLottoTicket.objects.filter(daily_lotto=latest_hourly).count()
        daily_revenue = DailyLotto.TICKET_PRICE * tickets
        six_prize = DailyLotto.JACKPOT_SHARE_RATE * daily_revenue
        # getting difference in time delta
        x = latest_hourly.end_date - timezone.now()
        ender = latest_hourly.end_date
        dato = parser.parse(str(ender))
        current_time = datetime.datetime.now()

        today_lotto = {
            'bought_tickets': tickets,
            'end_date': dato.isoformat(),
            'current_time': current_time.isoformat(),
            'count_down': convert_timedelta(x),
            'jackpot': previous_daily + six_prize
        }

        return Response({'response': today_lotto}, status=status.HTTP_200_OK)

    def post(self, request):
        latest_hourly = DailyLotto.objects.filter(lotto_type='H')[0]
        ends = latest_hourly.end_date

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

                DailyLottoTicket.objects.create(daily_lotto=latest_hourly, player_name=self.request.user, n1=n1,
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


class MultipleHourlyTicket(APIView):
    def get(self, request):
        latest_hourly = DailyLotto.objects.filter(lotto_type='H')[0]


        hourly_lotto = {
            'bought_tickets': DailyLottoTicket.objects.filter(daily_lotto=latest_hourly).count(),
            'start_date': latest_hourly.start_date,
            'count_down': latest_hourly.end_date - timezone.now()
        }

        return Response({'response': hourly_lotto}, status=status.HTTP_200_OK)

    def post(self, request):
        latest_hourly = DailyLotto.objects.filter(lotto_type='H')[0]
        ends = latest_hourly.end_date
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
                    create_random_tickets.delay(ticketno, latest_hourly.lotto_id, self.request.user.id)
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


class LottoStatView(APIView):
    def get(self, request):
        return Response(GamesHistorySerializer(Game_stat.objects.filter(user=request.user, game=lotto_game), many=True).data)


class Prev_and_next(viewsets.ViewSet):

    def past(self, request):
        m = DailyLotto.objects.all().order_by('-end_date')[1]
        n = DailyLottoTicket.objects.filter(daily_lotto=m)
        winners = n.filter(hits__gte=3).order_by('-hits')
        # place them on a list
        z = []
        details = {
            'draw_date':m.end_date,
            'jackpot': m.jack_pot,
            'n1': m.win1,
            'n2': m.win2,
            'n3': m.win3,
            'n4': m.win4,
            'n5': m.win5,
            'n6':m.win6,
            '6prize': n.filter(hits=6).count(),
            '5prize': n.filter(hits=5).count(),
            '4prize': n.filter(hits=4).count(),
            '3prize': n.filter(hits=3).count()

        }
        for winner in winners:
            username = winner.player_name.username
            tk = {'name':username, 'ticket_no':winner.ticket_no, 'hits':winner.hits}
            z.append(tk.copy())

        return Response({'response': details, 'past_winners':z}, status=status.HTTP_200_OK)

    def prev(self, request):
        m = DailyLotto.objects.filter(lotto_type='D').order_by('-end_date')
        newest = m[1]
        second_newest = next_in_order(newest, m)
        n = DailyLottoTicket.objects.filter(daily_lotto=second_newest)
        winners = n.filter(hits__gte=3).order_by('-hits')

        # place them on a list
        z = []
        details = {
            'draw_date': second_newest.end_date,
            'jackpot': second_newest.jack_pot,
            'n1': second_newest.win1,
            'n2': second_newest.win2,
            'n3': second_newest.win3,
            'n4': second_newest.win4,
            'n5': second_newest.win5,
            'n6': second_newest.win6,
            '6prize': n.filter(hits=6).count(),
            '5prize': n.filter(hits=5).count(),
            '4prize': n.filter(hits=4).count(),
            '3prize': n.filter(hits=3).count()

        }
        for winner in winners:
            username = winner.player_name.username
            tk = {'name': username, 'ticket_no': winner.ticket_no, 'hits': winner.hits}
            z.append(tk.copy())

        return Response({'response': details, 'past_winners': z}, status=status.HTTP_200_OK)

    def next(self, request):
        m = DailyLotto.objects.filter(lotto_type='D').order_by('-end_date')
        last = m[2]
        second_oldest = prev_in_order(last, m)

        n = DailyLottoTicket.objects.filter(daily_lotto=second_oldest)
        winners = n.filter(hits__gte=3).order_by('-hits')

        # place them on a list
        z = []
        details = {
            'draw_date': second_oldest.end_date,
            'jackpot': second_oldest.jack_pot,
            'n1': second_oldest.win1,
            'n2': second_oldest.win2,
            'n3': second_oldest.win3,
            'n4': second_oldest.win4,
            'n5': second_oldest.win5,
            'n6': second_oldest.win6,
            '6prize': n.filter(hits=6).count(),
            '5prize': n.filter(hits=5).count(),
            '4prize': n.filter(hits=4).count(),
            '3prize': n.filter(hits=3).count()

        }
        for winner in winners:
            username = winner.player_name.username
            tk = {'name': username, 'ticket_no': winner.ticket_no, 'hits': winner.hits}
            z.append(tk.copy())

        return Response({'response': details, 'past_winners': z}, status=status.HTTP_200_OK)
