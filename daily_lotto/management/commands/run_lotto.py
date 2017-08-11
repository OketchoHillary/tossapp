from django.core.management.base import BaseCommand
from daily_lotto.lotto_components import *


class Command(BaseCommand):

    help = 'daily lotto'

    def handle(self, *args, **options):

        create_lotto()
        countdown(60)
        print 'draw_starts'
        draw()