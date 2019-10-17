from django.core.management.base import BaseCommand
import schedule
import time

from lotto_api.quaterly_lotto import create_quaterly_lotto, quaterly_draw


class Command(BaseCommand):

    help = 'Tossapp lotto'

    def handle(self, *args, **options):
        schedule.every().day.at("16:26").do(create_quaterly_lotto)
        schedule.every().day.at("16:48").do(quaterly_draw)

        # schedule.every(6).hour.do(create_quaterly_lotto())
        # schedule.every(295).minutes.do(quaterly_draw)

        while True:
            schedule.run_pending()
            time.sleep(1)
