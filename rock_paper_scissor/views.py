from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.shortcuts import render

from accounts.models import Tuser
from rock_paper_scissor.forms import R_P_S_Form
from tossapp.models import Game, Game_stat


@login_required
def rock_paper_scissor(request):
    context = RequestContext(request)
    page = 'Rock Paper Scissor'
    page_brief = "Wrap, Cut and Crash. That's all you have to do."
    games = Game.objects.all()
    return render(request, 'rock_paper_scissor/index.html', locals(), context)


@login_required
@csrf_exempt
def reciver(request):
    x = Game.objects.filter(slug='rock-paper-scissor').values_list('id')[0]
    rps = int(x[0])
    if request.method == 'POST':
        form = R_P_S_Form(request.POST)
        if form.is_valid():
            bet = form.cleaned_data
            my_bet = bet.get('accountBalance')
            Tuser.objects.filter(username=request.user).update(balance=my_bet)
            Game.objects.filter(slug='rock-paper-scissor').update(times_played=F("times_played") + 1)
            Game_stat.objects.create(user=request.user, game__id=rps, bet_amount=my_bet, status=Game_stat.PENDING,
                                     service_fee=0)

    return render(request, 'rock_paper_scissor/reciver.html')

