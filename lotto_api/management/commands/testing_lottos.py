import random

from django.core.management import BaseCommand

from accounts_api.models import Tuser
from lotto_api.models import DailyLottoTicket, DailyLotto
from tauth.settings import NUMBER_RANGE
from tauth.task import create_random_tickets


class Command(BaseCommand):

    help = 'Tossapp lotto'

    def handle(self, *args, **options):
        ticket_num = 50
        players = Tuser.objects.filter(is_active=True)
        # daily lotto
        lotto = DailyLotto.objects.filter(lotto_type='D')[0]
        for p in players:
            print(p.id)
            create_random_tickets.delay(ticket_num, lotto.lotto_id, p.id)
        print('successfully')




