from django.conf.urls import url

from flip_coin.views import flip_coin

urlpatterns = [
    url(r'^dashboard/flip-coin$', flip_coin, name='flip_coin'),

    ]