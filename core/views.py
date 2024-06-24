# from django.shortcuts import render
from core.serializers import (
    OTPVerificationSerializer,
    UserCreateSerializer,
    UserSerializer,
)
from rest_framework.response import Response

# from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import get_user_model
from django.shortcuts import HttpResponse


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
                email=serializer.validated_data["email"],
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
        context = {
            "request": request,
        }
        serializer = UserCreateSerializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "message": "User Created Successfully",
            },
            status=status.HTTP_201_CREATED,
        )

    @swagger_auto_schema(
        request_body=OTPVerificationSerializer,
        method="PUT",
    )
    @action(detail=False, methods=["PUT"])
    def verify_otp(self, request):
        user = User.objects.get(
            email=request.data["email"],
        )
        serializer = OTPVerificationSerializer(
            instance=user,
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "details": "User has been successfully verified",
            },
            status=status.HTTP_200_OK,
        )


def activate(request):
    otp = request.GET.get("otp")
    serializer = OTPVerificationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    return HttpResponse(otp)
