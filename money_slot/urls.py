from django.conf.urls import url

from money_slot.views import money_slot

urlpatterns = [
    url(r'^dashboard/money-slot$', money_slot, name='money_slot'),

    ]