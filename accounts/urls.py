from django.urls import path
from accounts.views import tlogin

urlpatterns = [
    # url(r'^$',index, name='index'),
    path('login', tlogin, name='login'),

]
