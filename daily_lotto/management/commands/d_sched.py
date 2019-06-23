from django.core.management.base import BaseCommand
from daily_lotto.lotto_components import *
import schedule
import time


class Command(BaseCommand):

    help = 'Tossapp lotto'

    def handle(self, *args, **options):
        schedule.every(1).minutes.do(create_daily_lotto)
        # schedule.every(1).minutes.do(daily_draw)
        # schedule.every().day.at("23:55").do(daily_draw)
        #schedule.every().day.at("00:00").do(create_daily_lotto)

        # schedule.every().hour.do(draw)
        # schedule.every().monday.do(job)
        # schedule.every().wednesday.at("13:15").do(job)

        while True:
            schedule.run_pending()
            time.sleep(1)
