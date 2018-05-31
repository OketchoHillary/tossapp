from django.core.management.base import BaseCommand
from daily_lotto.lotto_components import *
import schedule
import time
from test_lotto import *


class Command(BaseCommand):

    help = 'Tossapp lotto'

    def handle(self, *args, **options):
        test_lotto_draw()

    
