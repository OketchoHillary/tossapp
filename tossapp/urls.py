from django.conf.urls import url, include

from tossapp.views import index, dashboard, dashboard_notifications, dashboard_games, dashboard_games_history, \
    dashboard_transactions, dashboard_payments_deposit, dashboard_payments_withdraw, dashboard_referrals, \
    dashboard_account_profile, dashboard_account_settings, contact, faq, rock_paper_scissor, flip_coin, money_slot, \
    faq_detail, dashboard_edit_profile

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^contact-us', contact, name='contact'),
    url(r'^faq$', faq, name='faq'),
    url(r'^faq/(?P<slug>[\w-]+)/$', faq_detail, name='faq_detail'),
    url(r'^dashboard$', dashboard, name='dashboard'),
    #url(r'^dashboard$', dashboard.as_view(), name='dashboard'),
    url(r'^dashboard/notifications$',dashboard_notifications.as_view(), name='dashboard_notifications'),
    url(r'^dashboard/games$',dashboard_games.as_view(), name='dashboard_games'),
    url(r'^dashboard/rock-paper-scissor$',rock_paper_scissor.as_view(), name='rock_paper_scissor'),
    url(r'^dashboard/flip-coin$',flip_coin.as_view(), name='flip_coin'),
    url(r'^dashboard/money-slot$',money_slot.as_view(), name='money_slot'),
    url(r'^dashboard/games-history$',dashboard_games_history.as_view(), name='dashboard_games_history'),
    url(r'^dashboard/transactions$',dashboard_transactions.as_view(), name='dashboard_transactions'),
    url(r'^dashboard/deposit$',dashboard_payments_deposit.as_view(), name='dashboard_payments_deposit'),
    url(r'^dashboard/withdraw$',dashboard_payments_withdraw.as_view(), name='dashboard_payments_withdraw'),
    url(r'^dashboard/referrals$',dashboard_referrals.as_view(), name='dashboard_referrals'),
    url(r'^dashboard/profile$',dashboard_account_profile.as_view(), name='dashboard_account_profile'),
    url(r'^dashboard/settings$',dashboard_account_settings.as_view(), name='dashboard_account_settings'),
    url(r'^dashboard/account-settings$',dashboard_edit_profile.as_view(), name='dashboard_edit_profile'),
   # url(r'^dashboard/account-settings$', edit_profile, name='edit_profile')
]