from django.urls import path
from rest_framework.authtoken import views

from api.views import *


urlpatterns = [
    # tossap account APIs
    path('create-user/', UserCreate.as_view(), name='createUserApi'),
    path('login/', LoginView.as_view(), name='loginUserApi'),
    path('activate-user/<str:username>/', VerificationAPI.as_view({'post': 'verify_user'}), name='verify_user_api'),
    path('view-verification/<str:username>', VerificationAPI.as_view({'get': 'get_verification_code'}),
         name='get_verification_code_api'),
    path('logout', LogoutView.as_view(), name='logoutUserApi'),
    path('user-profile/', ProfileView.as_view(), name='profileViewApi'),
    path('profile-update/', ProfileUpdateView.as_view(), name='profileUpdateApi'),
    path('username-update/', UsernameUpdateView.as_view(), name='usernameUpdateApi'),
    path('photo-update/', ProfilePicViewSet.as_view(), name='profilePhotoApi'),
    path('change-password/', ChangePasswordAPI.as_view({'put': 'pass_change'}), name='pass_change_api'),
    path('api-token-auth/', views.obtain_auth_token),
    path('authenticate/', CustomObtainAuthToken.as_view()),


]


