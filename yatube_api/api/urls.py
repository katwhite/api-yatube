from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import PostViewSet, GroupViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('', include(router.urls)),

    path('posts/<int:post_id>/comments/<int:pk>/', CommentViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
]

# api/v1/api-token-auth/ (POST) — передаём логин и пароль, получаем токен;
# api/v1/posts/ (GET, POST) — получаем список всех постов или создаём новый пост;
# api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE) — получаем, редактируем или удаляем пост с идентификатором {post_id};
# api/v1/groups/ (GET) — получаем список всех групп;
# api/v1/groups/{group_id}/ (GET) — получаем информацию о группе с идентификатором {group_id};

# api/v1/posts/{post_id}/comments/ (GET) — получаем список всех комментариев поста с идентификатором post_id (POST), создаём новый комментарий для поста с идентификатором {post_id};
# api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE) — получаем, редактируем или удаляем комментарий с идентификатором {comment_id} в посте с id=post_id.