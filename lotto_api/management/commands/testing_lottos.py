import random

from django.core.management import BaseCommand

from accounts_api.models import Tuser
from lotto_api.models import DailyLottoTicket, DailyLotto
from tauth.settings import NUMBER_RANGE


class Command(BaseCommand):

    help = 'Tossapp lotto'

    def handle(self, *args, **options):
        ticket_num = 500
        players = Tuser.objects.filter(is_active=True)
        # daily lotto
        daily = DailyLotto.objects.filter(lotto_type='H')[0]
        for p in players:
            for x in range(ticket_num):
                num1, num2, num3, num4, num5, num6 = random.sample(range(1, NUMBER_RANGE), 6)
                DailyLottoTicket.objects.create(player_name=p, daily_lotto=daily, n1=num1, n2=num2, n3=num3, n4=num4,
                                                n5=num5, n6=num6)
        print('successfully')




