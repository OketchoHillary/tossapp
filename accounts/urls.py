from django.conf.urls import url
from django.contrib.auth import views as auth_views
from accounts.views import activate, RegisterView, tlogin, change_number, forgot_password, new_pass, enter_code

urlpatterns = [
    # url(r'^$',index, name='index'),
    url(r'^login$', tlogin, name='login'),
    url(r'^logout$', auth_views.logout, name='logout'),
    url(r'^register/(?:(?P<username>\w+)/)?$', RegisterView.as_view(), name='register'),
    url(r'^activate/(?P<user>\w+)$', activate, name='activate'),
    url(r'^forgot-password$', forgot_password, name='forgot_password'),
    url(r'^enter-code/(?P<user>\w+)$', enter_code, name='enter_code'),
    url(r'^new-password/(?P<user>\w+)$', new_pass, name='new_pass'),
    url(r'^change_number/(?P<user>\w+)$', change_number, name='change_number'),
]
