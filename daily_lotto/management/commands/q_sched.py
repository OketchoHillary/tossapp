from django.core.management.base import BaseCommand
from daily_lotto.daily_l import *
import schedule
import time

from daily_lotto.quaterly_lotto import create_quaterly_lotto, quaterly_draw


class Command(BaseCommand):

    help = 'Tossapp lotto'

    def handle(self, *args, **options):

        # schedule.every(1).minutes.do(create_daily_lotto())
        # schedule.every(1).minutes.do(daily_draw)
        schedule.every(6).hour.do(create_quaterly_lotto())
        schedule.every(295).minutes.do(quaterly_draw)

        while True:
            schedule.run_pending()
            time.sleep(1)
