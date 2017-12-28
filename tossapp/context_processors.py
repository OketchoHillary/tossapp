import datetime

from daily_lotto.models import DailyLottoTicket, DailyLotto
from daily_lotto.views import todays_lotto
from tossapp.models import Game


def years_processor(request):
    year = datetime.date.today().year
    return {'year':year}


def games_processor(request):
    games = Game.objects.all()
    return {'games': games}


def current_lotto_processor(request):
    ticket_count = DailyLottoTicket.objects.filter(daily_lotto=todays_lotto()).count()
    daily_revenue = DailyLotto.TICKET_PRICE * ticket_count
    six_prize_pool = DailyLotto.JACKPOT_SHARE_RATE * daily_revenue
    w = DailyLotto.objects.all().values_list('jack_pot').order_by('-start_date')[1]
    pjackpot = int(w[0])
    current_lotto = pjackpot + six_prize_pool
    return {'current_lotto':current_lotto}

