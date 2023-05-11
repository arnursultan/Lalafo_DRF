from rest_framework.routers import DefaultRouter

from apps.users.views import UserAPIViewSet


router = DefaultRouter()
router.register('users', UserAPIViewSet, "api_users")

urlpatterns = router.urls