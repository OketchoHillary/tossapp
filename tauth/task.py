import random

from celery import shared_task

from lotto_api.models import DailyLottoTicket


@shared_task
def create_random_tickets(quantity, lotto_id, user_id):
    for i in range(quantity):
        generated_numbers = random.sample(range(1, 20), 6)
        t1, t2, t3, t4, t5, t6 = generated_numbers
        DailyLottoTicket.objects.create(player_name_id=user_id, daily_lotto_id=lotto_id,
                                        n1=t1, n2=t2, n3=t3, n4=t4, n5=t5, n6=t6)
    return '{} random tickets created with success!'.format(quantity)