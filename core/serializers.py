from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model
from random import randint
from django.core.mail import send_mail

User = get_user_model()


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255)


class UserCreateSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255)
    confirm_password = serializers.CharField(max_length=255)

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:

            raise ValidationError(
                {
                    "password_mismatch": "Passwords don't match",
                }
            )
        if User.objects.filter(email=attrs["email"]).exists():
            raise ValidationError({"email": "email already exists"})

        return attrs

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        user = User.objects.create_user(**validated_data)
        otp = randint(0000, 9999)

        user.otp = otp
        user.save()
        subject = "Registration Successful"
        request = self.context["request"]
        # raise Exception(request.get_host())
        activation_link = f"{request.get_host()}?otp={otp}"
        message = f"""Hi {user.username},
        thank you for registering,
        Your OTP for activating your account is {otp}
        for {user.email}
        Your Activation link {activation_link}
        """
        email_from = "info@meropasal.com"
        recipient_list = [
            user.email,
        ]
        send_mail(subject, message, email_from, recipient_list)

        return user


class OTPVerificationSerializer(serializers.Serializer):
    otp = serializers.IntegerField()
    email = serializers.EmailField()

    # def validate(self, attrs):
    # if User.objects.filter(email=attrs["email"]).exists():
    #     user = User.objects.get(email=attrs["email"])
    #     if user.otp == attrs["otp"]:
    #         return attrs
    #     else:
    #         raise ValidationError({"otp": "Invalid OTP"})
    # else:
    #     raise ValidationError({"email": "Invalid Email"})

    def validate(self, attrs):
        user = User.objects.filter(
            email=attrs["email"],
            otp=attrs["otp"],
        ).exists()
        if not user:
            raise ValidationError(
                {
                    "otp": "Invalid OTP",
                }
            )
        return attrs

    def update(self, instance, validate_data):
        instance.is_active = True
        instance.save()
        return instance
