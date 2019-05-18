"""
from daily_lotto.models import *
import random


def create_lotto():

    # creating lotto
    l1 = DailyLotto.objects.create()
    print(l1)
    #time.sleep(300)

    print('starting the draw')

    ticket_count = DailyLottoTicket.objects.filter(purchased_time__contains=datetime.date.today()).count()

    l2 = DailyLotto.objects.filter(start_date__contains=datetime.date.today() - datetime.timedelta(1))

    previous_hse_com = DailyQuota.objects.filter(daily_lotto=l2).values_list('house_commission')
    ph = list(previous_hse_com[0])
    previoushsecom = ph[0]

    # House share
    commission_prize = DailyLotto.TICKET_PRICE * DailyLotto.HOUSE_COMMISSION_RATE
    house_pool = ticket_count * commission_prize

    # new hse commission sum
    new_hse_sum = previoushsecom + house_pool

    # update my database
    CommissionSum.objects.create(commission_total=new_hse_sum)

    # Six share
    six_prize = DailyLotto.TICKET_PRICE * DailyLotto.JACKPOT_SHARE_RATE
    six_prize_pool = ticket_count * six_prize

    # Five share
    five_prize = DailyLotto.TICKET_PRICE * DailyLotto.FIVE_SHARE_RATE
    five_prize_pool = ticket_count * five_prize

    # Four share
    four_prize = DailyLotto.TICKET_PRICE * DailyLotto.FOUR_SHARE_RATE
    four_prize_pool = ticket_count * four_prize

    # Three share
    three_prize = DailyLotto.TICKET_PRICE * DailyLotto.THREE_SHARE_RATE
    three_prize_pool = ticket_count * three_prize

    # updating quotas
    DailyQuota.objects.filter(daily_lotto=l1).update(house_commission=house_pool, six_number_prize_pool=six_prize_pool,five_number_prize_pool=five_prize_pool,
                                                     four_number_prize_pool=four_prize_pool,three_number_prize_pool=three_prize_pool)

    # previous jackpot
    previousJackpot = DailyLotto.objects.filter(start_date__contains=datetime.date.today() - datetime.timedelta(1)).values_list('jack_pot')
    pj = list(previousJackpot[0])
    pjackpot = pj[0]

    # retrieving today's six_prize pool quota
    current_sixQuota = DailyQuota.objects.filter(daily_lotto=l1).values_list('six_number_prize_pool')
    cq = list(current_sixQuota[0])
    current_quota = cq[0]

    # jackpot
    jackpot = pjackpot + current_quota

    # updating current jackpot
    DailyLotto.objects.filter(start_date__contains=datetime.date.today()).update(jack_pot=jackpot)

    # creating winning numbers
    number_pool = random.sample(xrange(1, 50), 6)
    num1, num2, num3, num4, num5, num6 = number_pool
    DailyLotto.objects.filter(start_date__contains=datetime.date.today()).update(win1=num1, win2=num2, win3=num3, win4=num4, win5=num5, win6=num6)

    for ticket in DailyLottoTicket.objects.filter(purchased_time__contains=datetime.date.today()):

        winning_numbers = DailyLotto.objects.filter(start_date__contains=datetime.date.today()).values_list('win1','win2','win3',
                                                                                                   'win4', 'win5','win6')
        lucky_numbers = list(winning_numbers[0])
        ticket_numbers = [z for z in [int(y) for y in str(ticket).split(',')]]
        matches = set(lucky_numbers).intersection(set(ticket_numbers))

        # Getting the winning ticket
        c2 = ticket

        # Getting the winning player
        p2 = ticket.player_name

        # update ticket hits field
        ticket.hits = hits = len(list(matches))
        ticket.save()

        # create winning tickets greater than 3
        if len(list(matches)) >= 3:
            DailyLottoResult.objects.create(hits_number_prize=len(list(matches)), prize=0, daily_lotto_ticket=c2,
                                            winners=p2)

        # Commissions
        a = DailyLottoTicket.objects.filter(purchased_time__contains=datetime.date.today(), hits=3).count()
        b = DailyLottoTicket.objects.filter(purchased_time__contains=datetime.date.today(), hits=4).count()
        c = DailyLottoTicket.objects.filter(purchased_time__contains=datetime.date.today(), hits=5).count()
        d = DailyLottoTicket.objects.filter(purchased_time__contains=datetime.date.today(), hits=6).count()

        # backupJackpot
        backup = DailyLotto.objects.filter(start_date__contains=datetime.date.today() - datetime.timedelta(1)).values_list('backup_jackpot')
        bu = list(backup[0])
        backupJackpot = bu[0]

        pool6 = DailyLotto.objects.filter(start_date__contains=datetime.date.today()).values_list('jack_pot')
        x = list(pool6[0])
        my_pool6 = x[0]

        pool5 = DailyQuota.objects.filter(daily_lotto=l1).values_list('five_number_prize_pool')
        y = list(pool5[0])
        my_pool5 = y[0]

        pool4 = DailyQuota.objects.filter(daily_lotto=l1).values_list('four_number_prize_pool')
        z = list(pool4[0])
        my_pool4 = z[0]

        pool3 = DailyQuota.objects.filter(daily_lotto=l1).values_list('three_number_prize_pool')
        v = list(pool3[0])
        my_pool3 = v[0]

        # commissions

        if d >= 1:
            for6 = my_pool6 / d
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
            DailyQuota.objects.filter(daily_lotto=l1).update(three_number_prize_pool_commission=for3)
            DailyLottoResult.objects.filter(draw_date__contains=datetime.date.today(), hits_number_prize=3).update(prize=for3)
            DailyLottoTicket.objects.filter(purchased_time__contains=datetime.date.today(), hits=3).update(ticket_prize=for3)

        if len(list(matches)) == 4:
            DailyQuota.objects.filter(daily_lotto=l1).update(four_number_prize_pool_commission=for4)
            DailyLottoResult.objects.filter(draw_date__contains=datetime.date.today(), hits_number_prize=4).update(prize=for4)
            DailyLottoTicket.objects.filter(purchased_time__contains=datetime.date.today(), hits=4).update(ticket_prize=for4)

        if len(list(matches)) == 5:
            DailyQuota.objects.filter(daily_lotto=l1).update(five_number_prize_pool_commission=for5)
            DailyLottoResult.objects.filter(draw_date__contains=datetime.date.today(), hits_number_prize=5).update(prize=for5)
            DailyLottoTicket.objects.filter(purchased_time__contains=datetime.date.today(), hits=5).update(ticket_prize=for5)

        if len(list(matches)) == 6:
            DailyQuota.objects.filter(daily_lotto=l1).update(six_number_prize_pool_commission=for6)
            DailyLottoResult.objects.filter(draw_date__contains=datetime.date.today(), hits_number_prize=6).update(prize=for6)
            DailyLotto.objects.filter(start_date__contains=datetime.date.today()).update(jack_pot=backupJackpot, backup_jackpot=0)
            DailyLottoTicket.objects.filter(purchased_time__contains=datetime.date.today(), hits=6).update(ticket_prize=for6)

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

        my_backup_jackpot = backupJackpot + no3 + no4 + no5

        DailyLotto.objects.filter(start_date__contains=datetime.date.today()).update(backup_jackpot=my_backup_jackpot)

    print("done")



"""