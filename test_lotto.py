import os
import sys

from accounts.models import *
from daily_lotto.daily_l import *
from tauth.settings import NUMBER_RANGE

def test_lotto_draw():
    ticket_num = 1500
    hillary = Tuser.objects.get(username='Hillary')
    # my_lotto2 = DailyLotto.objects.create()
    my_lotto = DailyLotto.objects.all()[0]

    for x in range(ticket_num):
        num1, num2, num3, num4, num5, num6 = random.sample(xrange(1,NUMBER_RANGE),6)
        htick = DailyLottoTicket.objects.create(player_name=hillary,daily_lotto=my_lotto,n1=num1,n2=num2, n3=num3, n4=num4, n5=num5, n6=num6)

    kamoga = Tuser.objects.get(username='Kamoga_e')

    for x in range(ticket_num):
        num1, num2, num3, num4, num5, num6 = random.sample(xrange(1, NUMBER_RANGE), 6)
        ktick = DailyLottoTicket.objects.create(player_name=kamoga, daily_lotto=my_lotto, n1=num1, n2=num2, n3=num3, n4=num4, n5=num5, n6=num6)

    emma = Tuser.objects.get(username='Emma_m')

    for x in range(ticket_num):
        num1, num2, num3, num4, num5, num6 = random.sample(xrange(1, NUMBER_RANGE), 6)
        etick = DailyLottoTicket.objects.create(player_name=emma, daily_lotto=my_lotto, n1=num1, n2=num2, n3=num3, n4=num4, n5=num5, n6=num6)
    
    draw()

# if __name__ == "__main__":
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tauth.settings")
#     test_lotto_draw()

