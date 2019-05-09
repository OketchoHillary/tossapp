from django.conf.urls import url
from lotto_api.views import TicketDailyCreate

urlpatterns = [
    # ticket buy APIs
    url(r'^get-ticket', TicketDailyCreate.as_view({'post':'my_tickets'}), name='my_tickets'),
]


