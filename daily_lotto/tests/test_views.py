from django.test import TestCase
from lotto.daily_lotto.models import DailyLottoTicket, DailyLotto
import unittest

class IndexTest(TestCase):
    def setUp(self):
        pass

    def test_index_returns_correct_html(self):
        response = self.client.get('/')
        # expected_html = render_to_string('../templates/daily_lotto/home.html')
        self.assertIn('<h1>Daily Lotto</h1>',response.content)

    # def test_player_is_picked(self):
    #     player = Player()In
    #     player.save()

    def test_can_save_ticket(self):
        postObj = {'player':'Hillary',
                   'daily_lotto':'2017-01-14 17:02',
                   'num1':'2','num2':'39','num3':'25','num4':'28','num5':'12','num6':'6'
                   }
        response = self.client.post('/',postObj,follow=True)
        self.assertEqual('Hillary', DailyLottoTicket.objects.get(daily_lotto='2017-01-14 17:02'))






