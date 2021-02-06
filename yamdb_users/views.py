import hashlib

from django.conf import settings
from django.core.mail import send_mail
from rest_framework import status, viewsets
from rest_framework.decorators import action, api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .permissions import IsAdmin
from .serializers import (EmailSerializer, UserSerializer,
                          YamdbAuthTokenSerializer)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = "page_size"
    max_page_size = 1000


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin, ]
    pagination_class = StandardResultsSetPagination
    lookup_field = "username"

    @action(methods=["get", "patch", ],
            detail=False,
            permission_classes=[IsAuthenticated, ])
    def me(self, request):
        if request.method == "GET":
            serializer = UserSerializer(request.user)
            return Response(data=serializer.data,
                            status=status.HTTP_200_OK)
        if request.method == "PATCH":
            serializer = UserSerializer(request.user,
                                        data=request.data,
                                        partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data,
                                status=status.HTTP_200_OK)
            return Response(data=serializer.errors,
                            status=status.HTTP_200_OK)


@api_view(["POST", ])
def sent_email(request):
    serializer = EmailSerializer(data=request.data)
    email = request.data.get("email", False)
    if serializer.is_valid():
        if User.objects.filter(email=email).first():
            return Response("This email already register")
        hash_email = hashlib.sha256(email.encode("utf-8")).hexdigest()
        send_mail(
            "Confirm_registration",
            f"Your conformation code is {hash_email}",
            settings.EMAIL,
            [email, ],
            fail_silently=False, )
        return Response(f"check your mail for conformation code {email}",
                        status=status.HTTP_200_OK)

    return Response(serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)


class YamdbTokenObtainPairView(TokenObtainPairView):
    serializer_class = YamdbAuthTokenSerializer
