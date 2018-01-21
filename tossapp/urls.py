from django.conf.urls import url, include

from tossapp.views import index, dashboard, dashboard_notifications, dashboard_games, dashboard_games_history, \
    dashboard_transactions, dashboard_payments_deposit, dashboard_payments_withdraw, dashboard_referrals, \
    dashboard_account_profile, dashboard_account_settings, contact, faq, \
    edit_profile, how_it_works, about_us, notification_status, Toc, Privacy_policy, Career, \
    Latest_events

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^contact-us', contact, name='contact'),
    url(r'^faq$', faq.as_view(), name='faq'),
    url(r'^tac$', Toc.as_view(), name='tac'),
    url(r'^privacy$', Privacy_policy.as_view(), name='privacy'),
    url(r'^career$', Career.as_view(), name='career'),
    url(r'^latest-events$', Latest_events.as_view(), name='Latest_events'),
    url(r'^mark_as_read/(?P<n_id>\d+)/$', notification_status, name='notification_status'),
    url(r'^how-it-works', how_it_works, name='how_it_works'),
    url(r'^about-us', about_us, name='about_us'),
    url(r'^dashboard$', dashboard, name='dashboard'),
    #url(r'^dashboard$', dashboard.as_view(), name='dashboard'),
    url(r'^dashboard/notifications$',dashboard_notifications.as_view(), name='dashboard_notifications'),
    url(r'^dashboard/games$',dashboard_games.as_view(), name='dashboard_games'),
    url(r'^dashboard/games-history$',dashboard_games_history.as_view(), name='dashboard_games_history'),
    url(r'^dashboard/transactions$',dashboard_transactions.as_view(), name='dashboard_transactions'),
    url(r'^dashboard/deposit$',dashboard_payments_deposit.as_view(), name='dashboard_payments_deposit'),
    url(r'^dashboard/withdraw$',dashboard_payments_withdraw.as_view(), name='dashboard_payments_withdraw'),
    url(r'^dashboard/referrals$',dashboard_referrals.as_view(), name='dashboard_referrals'),
    url(r'^dashboard/profile$',dashboard_account_profile.as_view(), name='dashboard_account_profile'),
    url(r'^dashboard/settings$',dashboard_account_settings.as_view(), name='dashboard_account_settings'),
    #url(r'^dashboard/account-settings$',dashboard_edit_profile.as_view(), name='dashboard_edit_profile'),
    url(r'^dashboard/account-settings$', edit_profile, name='edit_profile')
]