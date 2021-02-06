from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet

v1router = DefaultRouter()
v1router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments'
)

urlpatterns = [
    path('v1/', include(v1router.urls)),
]
