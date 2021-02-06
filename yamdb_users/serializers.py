import hashlib

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            "first_name",
            "last_name",
            "username",
            "bio",
            "email",
            "role"]
        model = User


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class YamdbAuthTokenSerializer(serializers.Serializer):
    password = serializers.CharField(required=False)
    email = serializers.EmailField()
    conformation_code = serializers.CharField()

    class Meta:
        model = User
        fields = ("email", "password", "conformation_code")

    def validate_token(self, data):
        super().validate()
        email = self.initial_data["email"]
        hash_email = hashlib.sha256(email.encode("utf-8")).hexdigest()
        conformation_code = data["conformation_code"]

        if hash_email != conformation_code:
            raise serializers.ValidationError("credential dosen't match")

        user = User.objects.create_user(email=email,
                                        password=conformation_code)

        refresh = TokenObtainPairSerializer.get_token(user)
        data["token"] = str(refresh.access_token)
        return data
