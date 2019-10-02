from django.core.management.base import BaseCommand
from lotto_api.daily_l import *
import schedule
import time


class Command(BaseCommand):

    help = 'Tossapp lotto'

    def handle(self, *args, **options):
        # schedule.every(10).minutes.do(create_daily_lotto)
        # schedule.every(11).minutes.do(daily_draw)
        schedule.every().day.at("16:57").do(create_daily_lotto)
        schedule.every().day.at("17:03").do(daily_draw)

        while True:
            schedule.run_pending()
            time.sleep(1)
