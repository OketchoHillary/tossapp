from django.conf.urls import url
from api.views import *


urlpatterns = [
    # tossap account APIs
    url(r'^create-user', UserCreate.as_view(), name='createUserApi'),
    url(r'^login', LoginView.as_view(), name='loginUserApi'),
    url(r'^logout', LogoutView.as_view(), name='logoutUserApi'),
    url(r'^user-profile/(?:(?P<username>\w+)/)?$', ProfileView.as_view({'get': 'get_this_profile'}), name='profileViewApi'),
    url(r'^profile-update/(?:(?P<username>\w+)/)?$', ProfileView.as_view({'put': 'update_profile'}), name='profileUpdateApi'),

]


