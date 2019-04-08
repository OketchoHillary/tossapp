from django.conf.urls import url

from tossapp.views import index, contact, faq, how_it_works, about_us, notification_status, Toc, Privacy_policy,\
    Career, Latest_events

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^contact-us$', contact, name='contact'),
    url(r'^faq$', faq.as_view(), name='faq'),
    url(r'^tac$', Toc.as_view(), name='tac'),
    url(r'^privacy$', Privacy_policy.as_view(), name='privacy'),
    url(r'^career$', Career.as_view(), name='career'),
    url(r'^latest-events$', Latest_events.as_view(), name='Latest_events'),
    url(r'^mark_as_read/(?P<n_id>\d+)/$', notification_status, name='notification_status'),
    url(r'^how-it-works', how_it_works, name='how_it_works'),
    url(r'^about-us', about_us, name='about_us'),
]