from django.core.management.base import BaseCommand
from lotto_api.daily_l import *
import schedule
import time


class Command(BaseCommand):

    help = 'Tossapp lotto'

    def handle(self, *args, **options):
        # schedule.every(1).minutes.do(create_daily_lotto)
        # schedule.every(1).minutes.do(daily_draw)
        schedule.every().day.at("23:55").do(daily_draw)
        schedule.every().day.at("00:00").do(create_daily_lotto)

        while True:
            schedule.run_pending()
            time.sleep(1)
