"""
from __future__ import print_function
import random
from django.http import HttpResponse
from daily_lotto.lotto_components import todays_lotto
from daily_lotto.models import *
import datetime
from django.core import serializers
import json


def lotto_today(request):
    obj = DailyLotto.objects.get(start_date__startswith=datetime.datetime.now().isoformat().split('T')[0])
    data = serializers.serialize('json', [obj, ])
    struct = json.loads(data)
    data = json.dumps(struct[0])
    return HttpResponse(data, content_type="application/json")


def total(single_form, multiple_tickets_form):
    return single_form + multiple_tickets_form


def balance_calculator(lar, ry):
    return lar - ry


def random_tickets(tick, req):
    my_quantity = tick.cleaned_data
    quantity = my_quantity.get('quantity')

    if quantity >= 1:
        for random_qunatity in range(quantity):
            generated_numbers = random.sample(range(1, 51), 6)
            t1,t2,t3,t4,t5,t6 = generated_numbers
            DailyLottoTicket.objects.create(player_name=req.user, daily_lotto=todays_lotto(), n1=t1, n2=t2, n3=t3, n4=t4, n5=t5, n6=t6)


def previous_day_APi(request):
    my_s = DailyLotto.objects.filter(start_date=datetime.datetime.now()-datetime.timedelta(days=1))
    json_s = json.loads(serializers.serialize("json", my_s))
    for i, my_lotto in enumerate(my_s):
        json_s[i]['fields']['end_date'] = my_lotto.end_date
    return HttpResponse(json.dumps(json_s))







"""