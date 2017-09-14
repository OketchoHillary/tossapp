import random
import time
from daily_lotto.models import *
from tossapp.models import *
from django.db.models import F
from daily_lotto.views import todays_lotto, previous_lotto


def countdown(n):
    while n > 0:
        print (n)
        time.sleep(1)
        n = n-1
        if n == 0:
            print('draw_starting')


def commission():
    ticket_count = DailyLottoTicket.objects.filter(daily_lotto=todays_lotto()).count()
    print ticket_count
    # daily revenue
    daily_revenue = DailyLotto.TICKET_PRICE * ticket_count

    # house share
    house_pool = DailyLotto.HOUSE_COMMISSION_RATE * daily_revenue

    # Six share
    six_prize_pool = DailyLotto.JACKPOT_SHARE_RATE * daily_revenue

    # Five share
    five_prize_pool = DailyLotto.FIVE_SHARE_RATE * daily_revenue

    # Four share
    four_prize_pool = DailyLotto.FOUR_SHARE_RATE * daily_revenue

    # Three share
    three_prize_pool = DailyLotto.THREE_SHARE_RATE * daily_revenue

    DailyQuota.objects.filter(daily_lotto=todays_lotto()).update(house_commission=house_pool,
                                                                 six_number_prize_pool=six_prize_pool,
                                                                 five_number_prize_pool=five_prize_pool,
                                                                 four_number_prize_pool=four_prize_pool,
                                                                 three_number_prize_pool=three_prize_pool)

    previous_hse_com = DailyQuota.objects.filter(daily_lotto=previous_lotto()).values_list('house_commission')
    ph = list(previous_hse_com[0])
    previoushsecom = ph[0]

    # new hse commission sum
    new_hse_sum = previoushsecom + house_pool

    # update my database
    CommissionSum.objects.create(commission_total=new_hse_sum)

    return


def create_lotto():
    lotto = DailyLotto.objects.create(start_date=datetime.date.today())
    return lotto


def draw():
    lotto_game = Game.objects.filter(name='Daily Lotto')[0]

    print(todays_lotto())
    commission()

    # retrieving current lotto id
    toss_lotto = DailyLotto.objects.all().values_list('lotto_id').order_by('-start_date')[0]
    lottoid = int(toss_lotto[0])

    # previous jackpot
    my_p = DailyLotto.objects.all().values_list('jack_pot').order_by('-start_date')[1]
    pjackpot = int(my_p[0])

    # retrieving today's six_prize pool quota
    current_sixQuota = DailyQuota.objects.filter(daily_lotto=todays_lotto()).values_list('six_number_prize_pool')
    cq = list(current_sixQuota[0])
    current_quota = cq[0]

    # my jack pot
    jackpot = pjackpot + current_quota

    # updating current jackpot
    DailyLotto.objects.filter(lotto_id=lottoid).update(jack_pot=jackpot)

    # creating winning numbers
    number_pool = random.sample(xrange(1, 50), 6)
    num1, num2, num3, num4, num5, num6 = number_pool
    DailyLotto.objects.filter(lotto_id=lottoid).update(win1=num1, win2=num2, win3=num3, win4=num4, win5=num5, win6=num6)

    for ticket in DailyLottoTicket.objects.filter(daily_lotto=todays_lotto()):
        winning_numbers = DailyLotto.objects.filter(lotto_id=lottoid).values_list('win1', 'win2','win3', 'win4', 'win5', 'win6')
        lucky_numbers = list(winning_numbers[0])
        ticket_numbers = [z for z in [int(y) for y in str(ticket).split(',')]]
        matches = set(lucky_numbers).intersection(set(ticket_numbers))

        # Getting the winning ticket
        c2 = ticket

        # Getting the winning player
        p2 = ticket.player_name

        ticket.hits = len(list(matches))
        ticket.save(update_fields=["hits"])

        # creating winners
        if len(list(matches)) >= 3:
            DailyLottoResult.objects.create(daily_lotto=todays_lotto(), hits_number_prize=len(list(matches)), prize=0, daily_lotto_ticket=c2,
                                            winners=p2)

        # Commissions
        a = DailyLottoTicket.objects.filter(daily_lotto=todays_lotto(), hits=3).count()
        b = DailyLottoTicket.objects.filter(daily_lotto=todays_lotto(), hits=4).count()
        c = DailyLottoTicket.objects.filter(daily_lotto=todays_lotto(), hits=5).count()
        d = DailyLottoTicket.objects.filter(daily_lotto=todays_lotto(), hits=6).count()

        # backupJackpot
        bp = DailyLotto.objects.all().values_list('backup_jackpot').order_by('-lotto_id')[1]
        backup = int(bp[0])

        p6 = DailyLotto.objects.all().values_list('jack_pot').order_by('-lotto_id')[0]
        pool6 = int(p6[0])

        pool5 = DailyQuota.objects.filter(daily_lotto=todays_lotto()).values_list('five_number_prize_pool')
        y = list(pool5[0])
        my_pool5 = y[0]

        pool4 = DailyQuota.objects.filter(daily_lotto=todays_lotto()).values_list('four_number_prize_pool')
        z = list(pool4[0])
        my_pool4 = z[0]

        pool3 = DailyQuota.objects.filter(daily_lotto=todays_lotto()).values_list('three_number_prize_pool')
        v = list(pool3[0])
        my_pool3 = v[0]

        # commissions

        if d >= 1:
            for6 = pool6 / d
        else:
            for6 = 0

        if c >= 1:
            for5 = my_pool5 / c
            no5 = my_pool5
        else:
            for5 = 0
            no5 = 0

        if b >= 1:
            for4 = my_pool4 / b
            no4 = my_pool4
        else:
            for4 = 0
            no4 = 0

        if a >= 1:
            for3 = my_pool3 / a
            no3 = my_pool3
        else:
            for3 = 0
            no3 = 0

        if len(list(matches)) == 3:
            DailyQuota.objects.filter(daily_lotto=todays_lotto()).update(three_number_prize_pool_commission=for3)
            DailyLottoResult.objects.filter(daily_lotto=todays_lotto(), hits_number_prize=3).update(prize=for3)
            DailyLottoTicket.objects.filter(daily_lotto=todays_lotto(), hits=3).update(ticket_prize=for3)
            Tuser.objects.filter(username=p2).update(balance=F("balance") + for3)

        if len(list(matches)) == 4:
            DailyQuota.objects.filter(daily_lotto=todays_lotto()).update(four_number_prize_pool_commission=for4)
            DailyLottoResult.objects.filter(daily_lotto=todays_lotto(), hits_number_prize=4).update(prize=for4)
            DailyLottoTicket.objects.filter(daily_lotto=todays_lotto(), hits=4).update(ticket_prize=for4)
            Tuser.objects.filter(username=p2).update(balance=F("balance") + for4)

        if len(list(matches)) == 5:
            DailyQuota.objects.filter(daily_lotto=todays_lotto()).update(five_number_prize_pool_commission=for5)
            DailyLottoResult.objects.filter(daily_lotto=todays_lotto(), hits_number_prize=5).update(prize=for5)
            DailyLottoTicket.objects.filter(daily_lotto=todays_lotto(), hits=5).update(ticket_prize=for5)
            Tuser.objects.filter(username=p2).update(balance=F("balance") + for5)

        if len(list(matches)) == 6:
            DailyQuota.objects.filter(daily_lotto=todays_lotto()).update(six_number_prize_pool_commission=for6)
            DailyLottoResult.objects.filter(daily_lotto=todays_lotto(), hits_number_prize=6).update(prize=for6)
            DailyLotto.objects.filter(lotto_id=lottoid).update(jack_pot=backup, backup_jackpot=0)
            DailyLottoTicket.objects.filter(daily_lotto=todays_lotto(), hits=6).update(ticket_prize=for6)
            Tuser.objects.filter(username=p2).update(balance=F("balance") + for6)

        else:
            print 'No Lotto Winners'

        if len(list(matches)) > 2:
            Game_stat.objects.filter(user=p2, timestamp=datetime.date.today(), game=lotto_game).update(status=Game_stat.WIN)
        else:
            Game_stat.objects.filter(user=p2, timestamp=datetime.date.today(), game=lotto_game).update(status=Game_stat.LOSE)

        # if no 3 winners
        """

        if a == 0:
            no3 = my_pool3
        else:
            no3 = 0
        # if no 4 winners
        if b == 0:
            no4 = my_pool4
        else:
            no4 = 0
        # if no 5 winners
        if b == 0:
            no5 = my_pool5
        else:
            no5 = my_pool5
            """

        my_backup_jackpot = backup + no3 + no4 + no5

        DailyLotto.objects.filter(lotto_id=lottoid).update(backup_jackpot=my_backup_jackpot)
