from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render

from tossapp.models import Game


@login_required
@csrf_protect
def compound_boxes(request):
    context = RequestContext(request)
    page = 'Sky boxes'
    page_brief = ""
    games = Game.objects.all()
    return render(request, 'sky_boxes/index.html', locals(), context)

