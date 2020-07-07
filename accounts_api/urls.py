from django.urls import path
from rest_framework.authtoken import views

from accounts_api.views import UserCreate, LoginView, VerificationAPI, LogoutView, ProfileView, ProfileUpdateView, \
    UsernameUpdateView, PhoneNumberUpdateView, ProfilePicViewSet, ChangePasswordAPI, ForgotPassword, ResetCode, \
    PasswordReset, ResendCode

urlpatterns = [
    # account APIs
    path('create-user/', UserCreate.as_view(), name='createUserApi'),
    path('login/', LoginView.as_view(), name='loginUserApi'),
    path('activate-user/', VerificationAPI.as_view({'post':'verify_user'}), name='verify_user_api'),
    path('logout/', LogoutView.as_view(), name='logoutUserApi'),
    path('user-profile/', ProfileView.as_view(), name='profileViewApi'),
    path('profile-update/', ProfileUpdateView.as_view(), name='profileUpdateApi'),
    path('username-update/', UsernameUpdateView.as_view({'put': 'username_change'}), name='usernameUpdateApi'),
    path('get-username/', UsernameUpdateView.as_view({'get': 'get_username'}), name='usernameUpdateApi'),
    path('phone-number-update/', PhoneNumberUpdateView.as_view({'put': 'phone_change'}), name='phoneNoUpdateApi'),
    path('show-number/', PhoneNumberUpdateView.as_view({'get': 'get_phone_no'}), name='phoneNoUpdateApi'),
    path('photo-update/', ProfilePicViewSet.as_view(), name='profilePhotoApi'),
    path('change-password/', ChangePasswordAPI.as_view(), name='pass_change_api'),
    path('forgot-password/', ForgotPassword.as_view(), name='forgot_password'),
    path('reset-code/<str:username>/', ResetCode.as_view(), name='reset_code'),
    path('reset-password/<str:username>/', PasswordReset.as_view(), name='password_reset'),
    path('resend-code/', ResendCode.as_view({'get': 'resend_code'}), name='resend_code'),
    path('accounts_api-token-auth/', views.obtain_auth_token),



]


