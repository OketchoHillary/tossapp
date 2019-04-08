from django.conf.urls import url
from tossapp_api.views import *


urlpatterns = [
    # tossap account APIs
    url(r'^users-notifications/(?:(?P<username>\w+)/)?$', NotificationView.as_view(), name='notificationApi'),
    url(r'^games-api', GameAPIView.as_view(), name='gameAPIView'),
    url(r'^user-refferals/(?:(?P<username>\w+)/)?$', ReferralAPI.as_view(), name='referralAPI'),
    url(r'^game-history-api/(?:(?P<username>\w+)/)?$', GameStatView.as_view(), name='game_stat_view'),
    url(r'^transaction-history-api/(?:(?P<username>\w+)/)?$', TransactionView.as_view(), name='trans_hist_view'),
]
