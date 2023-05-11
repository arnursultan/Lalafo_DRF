from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path

from apps.users.views import UserAPIViewSet


router = DefaultRouter()
router.register('users', UserAPIViewSet, "api_users")

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name="api_login"),
    path('login/refresh/', TokenRefreshView.as_view(), name="api_token_refresh")
]

urlpatterns += router.urls