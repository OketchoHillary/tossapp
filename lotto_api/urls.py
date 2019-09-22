from django.urls import path

from lotto_api.views import *

urlpatterns = [
    # ticket buy APIs
    path('daily-get-ticket', TicketDailyCreate.as_view({'post': 'my_tickets'}), name='daily_tickets'),
    path('show-daily-get-ticket', TicketDailyCreate.as_view({'get': 'get_daily'}), name='display_daily_tickets'),

    path('daily-multiple-tickets', MultipleDailyTicket.as_view({'post': 'other_tickets'}), name='other_daily_tickets'),
    path('quaterly-get-ticket', TicketQuaterlyCreate.as_view({'post': 'my_tickets'}), name='quaterly_tickets'),
    path('quaterly-multiple-tickets', MultipleQuaterlyTicket.as_view({'post': 'other_tickets'}),
         name='other_quaterly_tickets'),
    path('hourly-get-ticket', TicketHourlyCreate.as_view({'post': 'my_tickets'}), name='hourly_tickets'),
    path('hourly-multiple-tickets', MultipleHourlyTicket.as_view({'post': 'other_tickets'}),
         name='other_hourly_tickets'),
    path('all-time-winners', AllTimeWinnersAPI.as_view(), name='AllTimeWinnersAPI'),
    path('<str:lotto_date>/', PreviousLottoAPI.as_view({'get': 'get_previous_lottos'}), name='PreviousLottoAPI'),
    path('lotto-stats', LottoStatView.as_view(), name='lotto_stat'),
 ]

