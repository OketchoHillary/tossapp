from django.urls import path

from lotto_api.views import TicketDailyCreate, MultipleDailyTicket, TicketQuaterlyCreate, MultipleQuaterlyTicket, \
    TicketHourlyCreate, MultipleHourlyTicket, AllTimeWinnersAPI, Prev_and_next, LottoStatView

urlpatterns = [
    # ticket buy APIs
    path('daily-get-ticket', TicketDailyCreate.as_view(), name='daily_tickets'),
    path('daily-multiple-tickets', MultipleDailyTicket.as_view(), name='other_daily_tickets'),
    path('quaterly-get-ticket', TicketQuaterlyCreate.as_view(), name='quaterly_tickets'),
    path('quaterly-multiple-tickets', MultipleQuaterlyTicket.as_view(),
         name='other_quaterly_tickets'),
    path('hourly-get-ticket', TicketHourlyCreate.as_view(), name='hourly_tickets'),
    path('hourly-multiple-tickets', MultipleHourlyTicket.as_view(),
         name='other_hourly_tickets'),
    path('all-time-winners', AllTimeWinnersAPI.as_view(), name='AllTimeWinnersAPI'),
    path('prev-lotto/', Prev_and_next.as_view({'get': 'prev'}), name='PrevLottoAPI'),
    path('next-lotto/', Prev_and_next.as_view({'get': 'next'}), name='NextLottoAPI'),
    path('past-lotto/', Prev_and_next.as_view({'get': 'past'}), name='PastLottoAPI'),
    path('lotto-stats', LottoStatView.as_view(), name='lotto_stat'),
 ]

