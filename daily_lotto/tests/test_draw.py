from django.test import TestCase
from daily_lotto.models import DailyLottoTicket, DailyLotto,Player
import datetime
from daily_lotto.operations import *
import unittest
import time

class DrawTest(TestCase):
    def setUp(self):
        # pass
        # self.dl = DailyLotto.objects.create()
        self.player_names = ['kamoga','Hillary','Oketcho','Edmund','Emma','Mupuya','Charles','Biddemu','Jack','Mark']
        for name in self.player_names:
            Player.objects.create(username=name)
        # for name in self.player_names:
        #     pl = Player.objects.get(username=name)
        #     for i in range(100):
        #         ticket = gen_ticket()
        #         DailyLottoTicket.objects.create(daily_lotto=self.dl,player=pl,n1=ticket[0],n2=ticket[1],
        #                                     n3=ticket[2],n4=ticket[3],n5=ticket[4],n6=ticket[5])

    def test_lotto_creation(self):
        self.assertEqual(self.dl, DailyLotto.objects.get(start_date__contains=datetime.date.today()))

    def test_create_players(self):
        self.assertTrue(len(Player.objects.all()) == 10)

    def test_create_tickets(self):
        self.assertTrue(len(DailyLottoTicket.objects.all()) == 10)

    def test_create_draw(self):
        pool = set([z for x in DailyLottoTicket.objects.all() for z in [int(y) for y in str(x).split(',')]])
        winning_numbers = get_winning_numbers(list(pool))
        # print winning_numbers

        for ticket in DailyLottoTicket.objects.all():
            ticket_numbers = [z for z in [int(y) for y in str(ticket).split(',')]]
            matches = set(winning_numbers).intersection(set(ticket_numbers))
            if len(list(matches)) > 3:
                print ticket.player,len(list(matches))

    def test_draw_multiple_times(self):
        for i in range(1000):
            dl = DailyLotto.objects.create()
            for name in self.player_names:
                pl = Player.objects.get(username=name)
                for b in range(100):
                    ticket = gen_ticket()
                    DailyLottoTicket.objects.create(daily_lotto=dl,player=pl,n1=ticket[0],n2=ticket[1],
                                            n3=ticket[2],n4=ticket[3],n5=ticket[4],n6=ticket[5])


            pool = set([z for x in DailyLottoTicket.objects.filter(daily_lotto=dl) for z in [int(y) for y in str(x).split(',')]])
            winning_numbers = get_winning_numbers(list(pool))
            # print winning_numbers

            for ticket in DailyLottoTicket.objects.filter(daily_lotto=dl):
                ticket_numbers = [z for z in [int(y) for y in str(ticket).split(',')]]
                matches = set(winning_numbers).intersection(set(ticket_numbers))
                if len(list(matches)) > 3:
                    print ticket.player,len(list(matches))

            time.sleep(10)

