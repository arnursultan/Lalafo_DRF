from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
import asyncio

from apps.posts.models import Post, FavoritePost
from apps.posts.serializer import PostSerializer, FavoritePostSerializer, PostDetailSerializer
from apps.posts.permission import PostPermission
from apps.telegram.views import send_message

# Create your views here.
class PostAPIViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        post = serializer.save(user=self.request.user)
        asyncio.run(send_message(-980643577, f"""Заявка на модерацию {post.id}
Название: {post.title}
Описание: {post.description}
Создан: {post.created}"""))
        return post
    
    def get_permissions(self):
        if self.action in ('create', ):
            return (IsAuthenticated(), )
        if self.action in ('update', 'partial_update', 'destroy'):
            return (IsAuthenticated(), PostPermission())
        return (AllowAny(), )
    
    def get_serializer_class(self):
        if self.action in ('retrieve', ):
            return PostDetailSerializer
        return PostSerializer
    
class FavoritePostAPIViewSet(GenericViewSet,
                             mixins.ListModelMixin,
                             mixins.CreateModelMixin,
                             mixins.DestroyModelMixin):
    queryset = FavoritePost.objects.all()
    serializer_class = FavoritePostSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action in ('destroy', ):
            return (PostPermission(), )
        return (AllowAny(), )