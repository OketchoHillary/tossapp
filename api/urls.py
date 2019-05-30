from django.conf.urls import url
from rest_framework.authtoken import views

from api.views import *


urlpatterns = [
    # tossap account APIs
    url(r'^create-user/$', UserCreate.as_view(), name='createUserApi'),
    url(r'^login', LoginView.as_view(), name='loginUserApi'),
    url(r'^activate-user/(?:(?P<username>\w+)/)?$', VerificationAPI.as_view({'post': 'verify_user'}), name='verify_user_api'),
    url(r'^view-verification/(?:(?P<username>\w+)/)?$', VerificationAPI.as_view({'get': 'get_verification_code'}),
        name='get_verification_code_api'),
    url(r'^logout', LogoutView.as_view(), name='logoutUserApi'),
    url(r'^user-profile/$', ProfileView.as_view(), name='profileViewApi'),
    url(r'^profile-update/$', ProfileUpdateView.as_view(), name='profileUpdateApi'),
    url(r'^username-update/$', UsernameUpdateView.as_view(), name='usernameUpdateApi'),
    url(r'^photo-update', ProfilePicViewSet.as_view(), name='profilePhotoApi'),
    url(r'^change-password/$', ChangePasswordAPI.as_view({'put': 'pass_change'}), name='pass_change_api'),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^authenticate/', CustomObtainAuthToken.as_view()),


]


