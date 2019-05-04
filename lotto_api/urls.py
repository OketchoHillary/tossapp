from django.conf.urls import url
from lotto_api.views import SingleTicketDailyCreate

urlpatterns = [
    # ticket buy APIs
    url(r'^get-ticket', SingleTicketDailyCreate.as_view({'post':'single_ticket'}), name='single_ticket_create'),
    url(r'^get-multiple-ticket', SingleTicketDailyCreate.as_view({'post':'multiple_ticket'}),
        name='multiple_ticket_create'),
]


