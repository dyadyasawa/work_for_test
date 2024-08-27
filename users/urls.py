
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.permissions import AllowAny
from users.apps import UsersConfig
from users.views import UserCreateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(permission_classes=(AllowAny,)), name="token_refresh"),

    path("list/", UserListApiView.as_view(), name="user-list"),
    path("detail/<int:pk>/", UserDetailApiView.as_view(), name="user-detail"),
    path("update/<int:pk>/", UserUpdateApiView.as_view(), name="user-update"),
    path("delete/<int:pk>/", UserDeleteApiView.as_view(), name="user-delete"),
]
