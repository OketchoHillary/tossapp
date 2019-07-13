from django.core.management.base import BaseCommand

from daily_lotto.hourly_lotto import create_hourly_lotto, hourly_draw
from daily_lotto.daily_l import *
import schedule
import time


class Command(BaseCommand):

    help = 'Tossapp lotto'

    def handle(self, *args, **options):

        schedule.every().hour.do(create_hourly_lotto)
        schedule.every(55).minutes.do(hourly_draw)

        while True:
            schedule.run_pending()
            time.sleep(1)
