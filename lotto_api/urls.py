from django.conf.urls import url
from lotto_api.views import *

urlpatterns = [
    # ticket buy APIs
    url(r'^daily-get-ticket$', TicketDailyCreate.as_view({'post':'my_tickets'}), name='daily_tickets'),
    url(r'^daily-multiple-tickets$', MultipleDailyTicket.as_view({'post':'other_tickets'}), name='other_daily_tickets'),
    # url(r'^quaterly-get-ticket$', TicketQuaterlyCreate.as_view({'post':'my_tickets'}), name='quaterly_tickets'),
    # url(r'^quaterly-multiple-tickets$', MultipleQuaterlyTicket.as_view({'post':'other_tickets'}), name='other_quaterly_tickets'),
    # url(r'^hourly-get-ticket$', TicketHourlyCreate.as_view({'post': 'my_tickets'}), name='hourly_tickets'),
    # url(r'^hourly-multiple-tickets$', MultipleHourlyTicket.as_view({'post': 'other_tickets'}),
        #name='other_hourly_tickets'),
    url(r'^all-time-winners', AllTimeWinnersAPI.as_view(), name='AllTimeWinnersAPI'),
    url(r'^(?P<lotto_date>.*)/$', PreviousLottoAPI.as_view({'get':'get_previous_lottos'}), name='PreviousLottoAPI'),
]



