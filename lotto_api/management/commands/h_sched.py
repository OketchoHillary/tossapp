from django.core.management.base import BaseCommand

from lotto_api.hourly_lotto import create_hourly_lotto, hourly_draw
import schedule
import time


class Command(BaseCommand):

    help = 'Tossapp lotto'

    def handle(self, *args, **options):
        # schedule.every().day.at("21:52").do(create_hourly_lotto)
        # schedule.every().day.at("21:55").do(hourly_draw)

        # schedule.every(1).hour.do(create_hourly_lotto)
        schedule.every(3).minutes.do(hourly_draw)

        while True:
            schedule.run_pending()
            time.sleep(1)
