from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from rest_framework.routers import DefaultRouter

from .views import UsersViewSet, YamdbTokenObtainPairView, sent_email

users_router = DefaultRouter()
users_router.register("", UsersViewSet)

router = DefaultRouter()

urls = [
    path("auth/email/", csrf_exempt(sent_email)),
    path("auth/token/", YamdbTokenObtainPairView.as_view()),
    path("users/", include(users_router.urls)),
    path("", include(router.urls)), ]

urlpatterns = [
    path('v1/', include(urls)),
]
