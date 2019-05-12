from django.conf.urls import url
from django.contrib.auth import views as auth_views
from accounts.views import tlogin

urlpatterns = [
    # url(r'^$',index, name='index'),
    url(r'^login$', tlogin, name='login'),

]
