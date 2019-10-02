
from django.urls import path
from tossapp_api.views import *


urlpatterns = [
    # tossap account APIs
    path('notifications-api', NotificationView.as_view({'get': 'list_not'}), name='notificationApi'),
    path('games-api', GameAPIView.as_view(), name='gameAPIView'),
    path('user-referrals', ReferralAPI.as_view(), name='referralAPI'),
    path('game-history-api', GameStatView.as_view(), name='game_stat_view'),
    path('transaction-history-api', TransactionHistoryView.as_view(), name='trans_hist_view'),
    path('deposit-funds/', TransactionView.as_view({'post': 'fund_deposit'}), name='fund_deposit_api'),
    path('withdraw-funds/', TransactionView.as_view({'post': 'fund_withdraw'}), name='fund_withdraw_api'),
]
