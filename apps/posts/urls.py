from rest_framework.routers import DefaultRouter

from apps.posts.views import PostAPIViewSet, FavoritePostAPIViewSet


router = DefaultRouter()
router.register('posts',  PostAPIViewSet, "api_posts")
router.register('favorite', FavoritePostAPIViewSet, "api_favorite_posts")

urlpatterns = router.urls