import datetime

from tossapp.models import Game


def years_processor(request):
    year = datetime.date.today().year
    return {'year':year}


def games_processor(request):
    games = Game.objects.all()
    return {'games': games}

