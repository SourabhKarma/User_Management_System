"""
URL configuration for ums project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


from user.api import UserRegistrationView,UserLoginView,UserNotiLoginView
from user.api import UserVerifyView,UserListView
from rest_framework import routers
from user.api import ResendOtpView,ResetPasswordView,UserActiveView,LogoutView


router = routers.DefaultRouter()



router.register(r'userdetail',UserListView)



urlpatterns = [
    path('api/v1/',include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/register/',UserRegistrationView.as_view()),
    path('api/otp/verify/',UserVerifyView.as_view()),
    path('api/otp/resend/',ResendOtpView.as_view()),
    path('api/login/', UserLoginView.as_view()),
    path('api/resetpassword/',ResetPasswordView.as_view()),
    path('api/logout/', LogoutView.as_view(), name='auth_logout'),

# ---- JWT TOKEN ------------
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "User Management System"