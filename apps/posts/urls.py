from rest_framework.routers import DefaultRouter

from apps.posts.views import PostAPIViewSet


router = DefaultRouter()
router.register('posts',  PostAPIViewSet, "api_posts")

urlpatterns = router.urls