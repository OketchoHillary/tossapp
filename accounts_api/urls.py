from django.urls import path
from rest_framework.authtoken import views

from accounts_api.views import *


urlpatterns = [
    # tossapp account APIs
    path('create-user/', UserCreate.as_view(), name='createUserApi'),
    path('login/', LoginView.as_view(), name='loginUserApi'),
    path('activate-user/<str:username>/', VerificationAPI.as_view({'post': 'verify_user'}), name='verify_user_api'),
    path('logout', LogoutView.as_view(), name='logoutUserApi'),
    path('user-profile/', ProfileView.as_view(), name='profileViewApi'),
    path('profile-update/', ProfileUpdateView.as_view(), name='profileUpdateApi'),
    path('username-update/', UsernameUpdateView.as_view(), name='usernameUpdateApi'),
    path('phone-number-update/', PhoneNumberUpdateView.as_view(), name='phoneNoUpdateApi'),
    path('photo-update/', ProfilePicViewSet.as_view(), name='profilePhotoApi'),
    path('change-password/', ChangePasswordAPI.as_view({'put': 'pass_change'}), name='pass_change_api'),
    path('forgot-password/', ForgotPassword.as_view(), name='forgot_password'),
    path('reset-code/<str:username>/', ResetCode.as_view({'post': 'post_code'}), name='reset_code'),
    path('reset-password/<str:username>/', PasswordReset.as_view({'put': 'reset_pass'}), name='password_reset'),
    path('resend-code/<str:username>/', ResendCode.as_view({'get': 'resend_code'}), name='resend_code'),
    path('accounts_api-token-auth/', views.obtain_auth_token),



]


