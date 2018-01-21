from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard/daily-lotto$', views.lotto, name='lotto'),
<<<<<<< HEAD
    url(r'^dashboard/daily-lotto/lotto_today$', views.lotto_today, name='lotto_today'),
    # url(r'^player_list/', views.index, name='player_list'),
    # url(r'^previous_list/$', ListView.as_view(queryset=DailyLotto.objects.filter(start_date__contains=datetime.date.today() - datetime.timedelta(1)), template_name='daily_lotto/home_list.html')),
    # url(r'^previous_list/(?P<pk>\d+)$', DetailView.as_view(model=DailyLotto, template_name='daily_lotto/home.html')),
    # url(r'^next_list/$', ListView.as_view(queryset=DailyLotto.objects.filter(start_date__contains=datetime.date.today() + datetime.timedelta(1)), template_name='daily_lotto/home.html')),
    # url(r'^next_list/(?P<pk>\d+)$', DetailView.as_view(model=DailyLotto, template_name='daily_lotto/home.html')),
=======
    url(r'^daily-lotto/previous-lotto$', views.previous_day_APi, name='previous_lotto'),
>>>>>>> 61521da6018f96cbc3b6a318e940b6ee934f0ada
    ]
