from django.conf.urls import url
from lotto_api.views import SingleTicketCreate

urlpatterns = [
    # ticket buy APIs
    url(r'^get-ticket', SingleTicketCreate.as_view(), name='single_ticket_create'),
]


