# from django.shortcuts import render
from core.serializers import UserCreateSerializer, UserSerializer
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your views here.
# using Api view decorator
""" @api_view(
    [
        "POST",
    ]
)
def login(request):
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )
        if user:
            token, _ = Token.objects.get_or_create(
                user=user,
            )
            return Response(
                {
                    "token": token.key,
                    "user": user.username,
                }
            )
        return Response(
            {
                "error": "Invalid credentials",

            },
            status=status.HTTP_401_UNAUTHORIZED,

        )


@api_view([
    "POST"
])
def register(request):
    serializer = UserCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(
        {
            "message": "User Created Successfully",

        },
        status=status.HTTP_201_CREATED,

    )
 """

# using classview


class UserViewSet(ViewSet):
    queryset = User.objects.all()

    @swagger_auto_schema(
        request_body=UserSerializer,
        method="POST",
    )
    @action(detail=False, methods=["POST"])
    def login(self, request):
        if request.method == "POST":
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = authenticate(
                username=serializer.validated_data["username"],
                password=serializer.validated_data["password"],
            )
            if user:
                token, _ = Token.objects.get_or_create(
                    user=user,
                )
                return Response(
                    {
                        "token": token.key,
                        "user": user.username,
                    }
                )
            return Response(
                {
                    "error": "Invalid credentials",

                },
                status=status.HTTP_401_UNAUTHORIZED,

            )

    @swagger_auto_schema(
        request_body=UserCreateSerializer,
        method="POST",
    )
    @action(detail=False, methods=["POST"])
    def register(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "message": "User Created Successfully",

            },
            status=status.HTTP_201_CREATED,

        )
