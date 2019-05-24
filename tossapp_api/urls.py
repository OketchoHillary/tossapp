
from django.conf.urls import url
from tossapp_api.views import *


urlpatterns = [
    # tossap account APIs
    url(r'^users-notifications', NotificationView.as_view(), name='notificationApi'),
    url(r'^games-api', GameAPIView.as_view(), name='gameAPIView'),
    url(r'^user-refferals', ReferralAPI.as_view(), name='referralAPI'),
    url(r'^game-history-api', GameStatView.as_view(), name='game_stat_view'),
    url(r'^transaction-history-api', TransactionHistoryView.as_view(), name='trans_hist_view'),
    url(r'^deposit-funds', TransactionView.as_view({'post': 'fund_deposit'}), name='fund_deposit_api'),
    url(r'^withdraw-funds', TransactionView.as_view({'post': 'fund_withdraw'}), name='fund_withdraw_api'),
]
