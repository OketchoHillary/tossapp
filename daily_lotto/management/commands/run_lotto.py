from django.core.management.base import BaseCommand
from daily_lotto.lotto_components import *
from threading import Timer
from datetime import datetime
import sched, time

#s = sched.scheduler(time.time, time.sleep)


class Command(BaseCommand):

    help = 'daily lotto'

    def handle(self, *args, **options):
        x = datetime.today()
        y = x.replace(day=x.day+1, hour=23, minute=55, second=0, microsecond=0)
        delta_t = y-x

        secs = delta_t.seconds+1

        def the_draw():
            draw()
        t = Timer(secs, the_draw())
        t.start()


"""
def do_something(sc):
    print 'Draw is starting'
    draw()
    print 'done'
    s.enter(30, 1, do_something, (sc,))
    s.enter(30, 1, do_something, (s,))
    s.run()
    """