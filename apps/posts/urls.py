from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from apps.posts.views import PostAPIViewSet


router = DefaultRouter()
router.register('posts',  PostAPIViewSet, "api_posts")

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name="api_login"),
    path('login/refresh', TokenRefreshView.as_view(), name="api_token_refresh"),
]

urlpatterns += router.urls