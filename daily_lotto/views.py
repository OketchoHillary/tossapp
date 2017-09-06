from __future__ import print_function

import random

from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect

from daily_lotto.forms import TicketForm, RandomTicketForm
from daily_lotto.models import *
from daily_lotto.tables import TicketTable
from tossapp.models import *
import datetime
from django_ajax.decorators import ajax


ends = str(now_plus_1())

my_lotto = DailyLotto.objects.all().values_list('lotto_id').order_by('-start_date')[0]
loto_id = int(my_lotto[0])
endDate = DailyLotto.objects.filter(lotto_id=loto_id).values_list('end_date', flat=True)

# Six share
six_prize = DailyLotto.TICKET_PRICE * DailyLotto.JACKPOT_SHARE_RATE

# Five share
five_prize = DailyLotto.TICKET_PRICE * DailyLotto.FIVE_SHARE_RATE

# Four share
four_prize = DailyLotto.TICKET_PRICE * DailyLotto.FOUR_SHARE_RATE

# Three share
three_prize = DailyLotto.TICKET_PRICE * DailyLotto.THREE_SHARE_RATE

# ticket cost
ticket_cost = 500

l0 = DailyLotto.objects.all()[0]


def total(single_form, multiple_tickets_form):

    return single_form + multiple_tickets_form


def balance_calculator(lar, ry):
    return lar - ry


def random_tickets(tick, req):
    my_quantity = tick.cleaned_data
    quantity = my_quantity.get('quantity')

    if quantity >= 1:
        for random_qunatity in range(quantity):
            generated_numbers = random.sample(xrange(1, 51),6)
            t1,t2,t3,t4,t5,t6 = generated_numbers
            DailyLottoTicket.objects.create(player_name=req.user, daily_lotto=l0, n1=t1, n2=t2, n3=t3, n4=t4, n5=t5, n6=t6)


# Selecting numbers
@login_required
@csrf_protect
def lotto(request, template_name='daily_lotto/home.html'):
    args = {}
    context = RequestContext(request)
    page = 'The Daily Lotto'
    page_brief = 'The more tickets you Buy, the more chances of moving away with the Jackpot.'
    player = request.user.username
    profile_pic = request.user.profile_photo.url
    full_name = request.user.get_my_full_name()
    # retrieving current user object
    current_user = Tuser.objects.filter(username=request.user)[0]
    # retrieving tickets from logged in user
    my_ticket_list = DailyLottoTicket.objects.filter(player_name=current_user).order_by('-purchased_time')
    table = TicketTable(DailyLottoTicket.objects.filter(player_name=current_user).order_by('-purchased_time'))
    table.paginate(page=request.GET.get('page', 1), per_page=10)
    lotto_game = Game.objects.filter(name='Daily Lotto')[0]
    tickets = DailyLottoTicket.objects.all()
    # quotas
    l1 = DailyLotto.objects.all()[1]
    # six pool and six prize winners
    pool6 = DailyQuota.objects.filter(daily_lotto=l1).values_list('six_number_prize_pool')
    x = list(pool6[0])
    pool6_winner = x[0]
    # counting tickets with 6 hits
    ticket_6hits = DailyLottoTicket.objects.filter(daily_lotto=l1, hits=6).count()
    # getting 6 commissions
    my_6 = DailyQuota.objects.filter(daily_lotto=l1).values_list('six_number_prize_pool_commission')
    r = list(my_6[0])
    commission6 = r[0]

    # five pool and five prize winners
    pool5 = DailyQuota.objects.filter(daily_lotto=l1).values_list('five_number_prize_pool')
    m = list(pool5[0])
    pool5_winner = m[0]
    # counting tickets with 5 hits
    ticket_5hits = DailyLottoTicket.objects.filter(daily_lotto=l1, hits=5).count()
    # getting 5 commissions
    my_5 = DailyQuota.objects.filter(daily_lotto=l1).values_list('five_number_prize_pool_commission')
    s = list(my_5[0])
    commission5 = s[0]

    # four pool and four prize winners
    pool4 = DailyQuota.objects.filter(daily_lotto=l1).values_list('four_number_prize_pool')
    n = list(pool4[0])
    pool4_winner = n[0]
    # counting tickets with 4 hits
    ticket_4hits = DailyLottoTicket.objects.filter(daily_lotto=l1, hits=4).count()
    # getting 4 commissions
    my_4 = DailyQuota.objects.filter(daily_lotto=l1).values_list('four_number_prize_pool_commission')
    t = list(my_4[0])
    commission4 = t[0]

    # three pool and three prize winners
    pool3 = DailyQuota.objects.filter(daily_lotto=l1).values_list('three_number_prize_pool')
    w = list(pool3[0])
    pool3_winner = w[0]
    # counting tickets with 3 hits
    ticket_3hits = DailyLottoTicket.objects.filter(daily_lotto=l1, hits=3).count()
    # getting 3 commissions
    my_3 = DailyQuota.objects.filter(daily_lotto=l1).values_list('three_number_prize_pool_commission')
    h = list(my_3[0])
    commission3 = h[0]

    # tickets sold
    sales = DailyLottoTicket.objects.filter(daily_lotto=l0).count()
    previous_sales = DailyLottoTicket.objects.filter(daily_lotto=l1).count()

    # number of winners
    number_of_winners = DailyLottoResult.objects.filter(daily_lotto=l1).count()

    # prize sum
    prize_sum = DailyLottoResult.objects.filter(daily_lotto=l1).aggregate(Sum('prize')).get('prize__sum', 0.00)

    """jackpot"""

    current6_quota = sales * six_prize

    # previous jackpot
    w = DailyLotto.objects.all().values_list('jack_pot').order_by('-start_date')[1]
    pjackpot = int(w[0])

    # my jack pot
    jackpot = pjackpot + current6_quota

    # lotto date
    draw_date = datetime.date.today()

    # result date
    previous_date = datetime.date.today() - datetime.timedelta(1)

    # winning numbers
    toss_lotto = DailyLotto.objects.all().values_list('lotto_id').order_by('-start_date')[1]
    lottoid = int(toss_lotto[0])
    winning_numbers = DailyLotto.objects.filter(lotto_id=lottoid)

    # previous winnings
    previous_winnings = DailyLotto.objects.filter(lotto_id=lottoid)

    # 6 hits winners
    number6Winners = DailyLottoTicket.objects.filter(daily_lotto=l1, hits=6).count()

    # 5 hits winners
    number5Winners = DailyLottoTicket.objects.filter(daily_lotto=l1, hits=5).count()

    # 4 hits winners
    number4Winners = DailyLottoTicket.objects.filter(daily_lotto=l1, hits=4).count()

    # 3 hits winners
    number3Winners = DailyLottoTicket.objects.filter(daily_lotto=l1, hits=3).count()

    # current users balance
    account_balance = request.user.balance

    dailyLottos = DailyLotto.objects.filter(lotto_id=lottoid)

    # previous winners
    dailyLottoResult_list = DailyLottoResult.objects.filter(daily_lotto=l1)

    # all time winners
    highest_winners = DailyLottoResult.objects.all().order_by('-prize')[:15]

    """Ticket purchase"""

    if request.method == 'POST':
        selection_form = TicketForm(request.POST)
        random_ticketform = RandomTicketForm(request.POST)
        # submitting both selection form and randomTickets form
        if selection_form.is_valid() and random_ticketform.is_valid():
            my_quantity = random_ticketform.cleaned_data
            quantity = my_quantity.get('quantity')
            if request.user.is_authenticated():
                # current time date and time is less than end date
                if datetime.datetime.now().isoformat() <= ends:
                    # players balance is greater or equal to 500
                    if request.user.balance >= 500:
                        # handling none type values

                        if quantity is None:
                            quantity = 0
                        else:
                            quantity = my_quantity.get('quantity')

                        # calculating number of tickets and ticket price
                        ze = quantity * ticket_cost
                        instance = selection_form.save(commit=False)
                        instance.player_name = request.user
                        instance.daily_lotto = l0
                        random_tickets(random_ticketform, request)
                        instance.save()
                        # calculating users balance
                        ao = balance_calculator(request.user.balance, ze + ticket_cost)
                        total_bet = ze + ticket_cost
                        # calculating service fee
                        excess_tickets = 25 * quantity
                        service_fee = 25 + excess_tickets
                        # updating users balance
                        Tuser.objects.filter(username=request.user).update(balance=ao)
                        Game_stat.objects.create(user=request.user, game=lotto_game, bet_amount=total_bet, status=3, service_fee=service_fee)
                        Game.objects.filter(name='Daily Lotto').update(times_played=F("times_played") + 1)
                        totals = total(ticket_cost, quantity * ticket_cost)
                        messages.success(request, "successfully submitted")
                        return HttpResponseRedirect(reverse_lazy('lotto'))
                    else:
                        messages.info(request, "insufficient balance")
                else:
                    messages.info(request, "Lotto has ended, Next lotto at midnight")

        # Submitting selection form only
        elif selection_form.is_valid():
            if request.user.is_authenticated():
                if datetime.datetime.now().isoformat() <= ends:
                    if request.user.balance >= 500:
                        instance1 = selection_form.save(commit=False)
                        instance1.player_name = request.user
                        instance1.daily_lotto = DailyLotto.objects.filter(start_date__contains=datetime.date.today())[0]
                        instance1.save()
                        ar = balance_calculator(request.user.balance, ticket_cost)
                        totals1 = total(ticket_cost, 0)
                        Tuser.objects.filter(user=request.user).update(balance=ar)
                        lotto_game = Game.objects.filter(name='Daily Lotto')[0]
                        Game_stat.objects.create(user=request.user, game=lotto_game, bet_amount=ticket_cost, status=3, service_fee=25)
                        Game.objects.filter(name='Daily Lotto').update(times_played=F("times_played") + 1)
                        #messages.success(request, "successfully submitted")
                        return HttpResponseRedirect(reverse_lazy('lotto'))
                    else:
                        messages.info(request, "Insufficient balance")
                else:
                    messages.info(request, "Lotto has ended, Next lotto at midnight")
            else:
                messages.info(request, "please Login")

        # submitting random ticket form only
        elif random_ticketform.is_valid():
            my_quantity2 = random_ticketform.cleaned_data
            quantity = my_quantity2.get('quantity')
            if request.user.is_authenticated():
                if datetime.datetime.now().isoformat() <= ends:
                    if request.user.balance >= 500:

                        if quantity is None:
                            quantity = 0
                        else:
                            quantity = my_quantity2.get('quantity')

                        random_tickets(random_ticketform, request)
                        ap = balance_calculator(request.user.balance, quantity * ticket_cost)
                        qt = quantity * ticket_cost
                        Tuser.objects.filter(username=request.user).update(balance=ap)
                        Game_stat.objects.create(user=request.user, game=lotto_game, bet_amount=qt, status=3, service_fee=25)
                        Game.objects.filter(name='Daily Lotto').update(times_played=F("times_played") + 1)
                        totals2 = total(0, quantity * ticket_cost)
                        messages.success(request, "successfully submitted")
                    else:
                        messages.info(request, "Insufficient balance")
                else:
                    messages.info(request, "Lotto has ended, Next lotto at midnight")
            return HttpResponseRedirect(reverse_lazy('lotto'))
    else:
        selection_form = TicketForm()
        random_ticketform = RandomTicketForm()
    args['random_ticketform'] = RandomTicketForm
    return render(request, template_name, locals(), context)







