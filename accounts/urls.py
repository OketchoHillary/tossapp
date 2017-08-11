from django.conf.urls import url, include
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import views as auth_views
from django.views.generic import CreateView
from accounts.admin import UserCreationForm
from accounts.views import activate, RegisterView, tlogin, change_number

urlpatterns = [
    # url(r'^$',index, name='index'),
    url(r'^login$', tlogin, name='login'),
    url(r'^logout$', auth_views.logout, name='logout'),
    url(r'^register/(?:(?P<username>\w+)/)?$', RegisterView.as_view(), name='register'),
    url(r'^activate/(?P<user>\w+)$', activate, name='activate'),
    url(r'^change_number/(?P<user>\w+)$', change_number, name='change_number'),
]
