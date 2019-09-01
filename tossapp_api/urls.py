
from django.urls import path
from tossapp_api.views import *


urlpatterns = [
    # tossap account APIs
    path('users-notifications', NotificationView.as_view(), name='notificationApi'),
    path('games-accounts_api', GameAPIView.as_view(), name='gameAPIView'),
    path('user-refferals', ReferralAPI.as_view(), name='referralAPI'),
    path('game-history-accounts_api', GameStatView.as_view(), name='game_stat_view'),
    path('transaction-history-accounts_api', TransactionHistoryView.as_view(), name='trans_hist_view'),
    path('deposit-funds/', TransactionView.as_view({'post': 'fund_deposit'}), name='fund_deposit_api'),
    path('withdraw-funds/', TransactionView.as_view({'post': 'fund_withdraw'}), name='fund_withdraw_api'),
]
