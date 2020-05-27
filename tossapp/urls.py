from django.urls import path

from tossapp.views import index, contact, faq, how_it_works, about_us, Toc, Privacy_policy, Career, Latest_events

urlpatterns = [
    path('', index, name='index'),
    path('contact-us/', contact, name='contact'),
    path('faq/', faq.as_view(), name='faq'),
    path('tac/', Toc.as_view(), name='tac'),
    path('privacy/', Privacy_policy.as_view(), name='privacy'),
    path('career/', Career.as_view(), name='career'),
    path('latest-events/', Latest_events.as_view(), name='Latest_events'),
    path('how-it-works/', how_it_works, name='how_it_works'),
    path('about-us/', about_us, name='about_us'),
]