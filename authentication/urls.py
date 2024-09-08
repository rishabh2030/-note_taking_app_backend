from django.contrib import admin
from django.urls import path,include
from .services.user_registration_api_view import UserRegistrationApiView
from .services.login_password_api_view import LoginPasswordApiView
from .services.login_otp_api_view import LoginOtpApiView
from .services.login_otp_verification_api_view import LoginOtpVerificationApiView
urlpatterns = [
    path("user-registration/",UserRegistrationApiView.as_view(),name="user-registration-api-view"),
    path("login-password/",LoginPasswordApiView.as_view(),name="login-password-api-view"),
    path("login-otp/",LoginOtpApiView.as_view(),name="login-otp-api-view"),
    path("login-otp-verification/",LoginOtpVerificationApiView.as_view(),name="login-otp-verification-api-view")
]