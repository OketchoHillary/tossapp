from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard/daily-lotto$', views.lotto, name='lotto'),
    url(r'^daily-lotto/previous-lotto$', views.previous_day_APi, name='previous_lotto'),
    ]
