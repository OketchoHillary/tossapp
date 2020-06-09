import random

from celery import shared_task
from celery.task import periodic_task
from celery.utils.log import get_task_logger
from datetime import timedelta

from lotto_api.daily_l import create_daily_lotto, daily_draw
from lotto_api.hourly_lotto import create_hourly_lotto, hourly_draw
from lotto_api.models import DailyLottoTicket
from lotto_api.quaterly_lotto import create_quaterly_lotto, quaterly_draw

logger = get_task_logger(__name__)


@shared_task
def create_random_tickets(quantity, lotto_id, user_id):
    for i in range(quantity):
        generated_numbers = random.sample(range(1, 20), 6)
        t1, t2, t3, t4, t5, t6 = generated_numbers
        DailyLottoTicket.objects.create(player_name_id=user_id, daily_lotto_id=lotto_id,
                                        n1=t1, n2=t2, n3=t3, n4=t4, n5=t5, n6=t6)
    return '{} random tickets created with success!'.format(quantity)


@periodic_task(run_every=timedelta(hours=24, minutes=0, seconds=30))
def run_create_daily_lotto():
    create_daily_lotto()
    logger.info("Daily lotto created")

@periodic_task(run_every=timedelta(hours=23, minutes=55, seconds=30))
def run_daily_draw():
    daily_draw()
    logger.info("Daily draw created")


@periodic_task(run_every=timedelta(hours=6, minutes=0, seconds=30))
def run_create_quarterly_lotto():
    create_quaterly_lotto()
    logger.info("Daily lotto created")

@periodic_task(run_every=timedelta(minutes=355, seconds=30))
def run_quarterly_draw():
    quaterly_draw()
    logger.info("Quarterly draw created")


@periodic_task(run_every=timedelta(hours=1, minutes=0, seconds=30))
def run_create_hourly_lotto():
    create_hourly_lotto()
    logger.info("Hourly lotto created")

@periodic_task(run_every=timedelta(minutes=55, seconds=30))
def run_hourly_raw():
    hourly_draw()
    logger.info("Hourly draw created")



# @app.task
# def run_daily_lotto():
#     create_daily_lotto()


