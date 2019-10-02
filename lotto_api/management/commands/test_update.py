import random

from django.core.management import BaseCommand

from lotto_api.daily_l import daily
from lotto_api.models import DailyLotto
from tauth.settings import NUMBER_RANGE


class Command(BaseCommand):

    help = 'Tossapp lotto'

    def handle(self, *args, **options):
        number_pool = random.sample(range(1, NUMBER_RANGE), 6)

        num1, num2, num3, num4, num5, num6 = number_pool
        DailyLotto.objects.filter(lotto_id=daily.lotto_id).update(win1=num1, win2=num2, win3=num3, win4=num4, win5=num5,
                                                                  win6=num6)
        print('successfully')
        print(daily)
