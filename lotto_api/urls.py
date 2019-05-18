"""
from django.conf.urls import url
from lotto_api.views import TicketDailyCreate, MultipleDailyTicket

urlpatterns = [
    # ticket buy APIs
    url(r'^get-ticket', TicketDailyCreate.as_view({'post':'my_tickets'}), name='my_tickets'),
    url(r'^multiple-tickets', MultipleDailyTicket.as_view({'post':'other_tickets'}), name='other_tickets'),
]
"""


