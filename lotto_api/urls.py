from django.conf.urls import url
from lotto_api.views import *

urlpatterns = [
    # ticket buy APIs
    url(r'^get-ticket$', TicketDailyCreate.as_view({'post':'my_tickets'}), name='my_tickets'),
    url(r'^multiple-tickets$', MultipleDailyTicket.as_view({'post':'other_tickets'}), name='other_tickets'),
    url(r'^all-time-winners', AllTimeWinnersAPI.as_view(), name='AllTimeWinnersAPI'),
    url(r'^(?P<lotto_date>\d{4}-\d{2}-\d{2})/$', PreviousLottoAPI.as_view({'get':'get_previous_lottos'}), name='PreviousLottoAPI'),
]



