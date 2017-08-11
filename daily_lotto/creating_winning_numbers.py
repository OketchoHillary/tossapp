import datetime
import random
from daily_lotto.models import DailyLotto, DailyLottoTicket


# gen winning numbers
def gen_winning_numbers():

    # creating the lotto
    DailyLotto.objects.create(start_date=datetime.date.today())

    # creating winning numbers
    number_pool = random.sample(xrange(1,51),6)
    # listobj = number_pool
    num1, num2, num3, num4, num5, num6 = number_pool
    val1 = num1
    val2 = num2
    val3 = num3
    val4 = num4
    val5 = num5
    val6 = num6

    #updating DailyLotto models
    DailyLotto.objects.filter(start_date__contains=datetime.date.today()).update(win1=val1, win2=val2, win3=val3,
                                                                                 win4=val4, win5=val5, win6=val6)

    #Retrieving winning numbers
    winning_numbers = DailyLotto.objects.filter(start_date__contains=datetime.date.today()).values_list('win1','win2','win3','win4'
                                                                                                        'win5','win6')

    # bought tickets
    drawn_tickets = DailyLottoTicket.objects.filter(purchased_time__contains=datetime.date.today()).values_list('n1',
                                                                                                                'n2','n3','n4','n5','n6')

    # Getting matches
    matches = list(set(winning_numbers).intersection(set(drawn_tickets)))





'''
DailyLotto.objects.filter(pk=1).update(win1=1)
YourModel.objects.filter(datetime_published=datetime(2008, 03, 27))
id = Place.objects.only('id').get(name='kansas').id
'''