from django.urls import path
# from .views import RegisterView, LogoutAPIView, SetNewPasswordAPIView, VerifyEmail, LoginAPIView, PasswordTokenCheckAPI, RequestPasswordResetEmail
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    # path('register/', RegisterView.as_view(), name="register"),
    # path('login/', LoginAPIView.as_view(), name="login"),
    # path('logout/', LogoutAPIView.as_view(), name="logout"),
    
]