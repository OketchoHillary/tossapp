from django.core.management.base import BaseCommand
from daily_lotto.lotto_components import *

import sched, time

s = sched.scheduler(time.time, time.sleep)


class Command(BaseCommand):

    help = 'daily lotto'

    def handle(self, *args, **options):
        def do_something(sc):
            create_lotto()
            countdown(120)
            print 'draw_starts'
            draw()
            print 'done'
            s.enter(600, 1, do_something, (sc,))
        s.enter(600, 1, do_something, (s,))
        s.run()