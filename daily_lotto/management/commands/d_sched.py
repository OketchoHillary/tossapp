from django.core.management.base import BaseCommand
from daily_lotto.lotto_components import *
import schedule
import time


class Command(BaseCommand):

    help = 'Tossapp lotto'

    def handle(self, *args, **options):

        # schedule.every(1).minutes.do(create_lotto)
        # schedule.every(1).minutes.do(draw)
<<<<<<< HEAD
=======
        schedule.every().day.at("23:55").do(draw)
        schedule.every().day.at("00:00").do(create_lotto)
>>>>>>> c59c1102ce3b06cedde3b1ab9a43bafc4b4a7cbc
        # schedule.every().hour.do(draw)
        schedule.every().day.at("00:00").do(create_lotto)
        schedule.every().day.at("23:55").do(draw)
        # schedule.every().monday.do(job)
        # schedule.every().wednesday.at("13:15").do(job)

        while True:
            schedule.run_pending()
            time.sleep(1)
