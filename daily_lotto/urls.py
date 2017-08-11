from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard/daily-lotto$', views.lotto, name='lotto'),
    # url(r'^player_list/', views.index, name='player_list'),
    # url(r'^previous_list/$', ListView.as_view(queryset=DailyLotto.objects.filter(start_date__contains=datetime.date.today() - datetime.timedelta(1)), template_name='daily_lotto/home_list.html')),
    # url(r'^previous_list/(?P<pk>\d+)$', DetailView.as_view(model=DailyLotto, template_name='daily_lotto/home.html')),
    # url(r'^next_list/$', ListView.as_view(queryset=DailyLotto.objects.filter(start_date__contains=datetime.date.today() + datetime.timedelta(1)), template_name='daily_lotto/home.html')),
    # url(r'^next_list/(?P<pk>\d+)$', DetailView.as_view(model=DailyLotto, template_name='daily_lotto/home.html')),
    ]
