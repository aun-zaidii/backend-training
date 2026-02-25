from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from .constants import (DEFAULT_FROM_EMAIL, REGISTRATION_EMAIL_MESSAGE,
                        REGISTRATION_EMAIL_SUBJECT)
from .serializers import (LoginRequestSerializer, LogoutRerquestSerializer,
                          RegisterRequestSerializer,
                          UpdateUserRequestSerialiizer, UserLoginSerializer,
                          UserRegistrationSerializer, UserUpdateSerializer)


class UserRegistrationView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request: Request) -> Response:
        try:
            request_serializer = RegisterRequestSerializer(data=request.data)
            request_serializer.is_valid(raise_exception=True)
            serializer = UserRegistrationSerializer(data=request_serializer.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            send_mail(
                REGISTRATION_EMAIL_SUBJECT,
                REGISTRATION_EMAIL_MESSAGE,
                DEFAULT_FROM_EMAIL,
                [request_serializer.data["email"]],
                fail_silently=False,
            )
            return Response(
                {"message": "User registered successfully"},
                status=status.HTTP_201_CREATED,
            )
        except ValidationError as e:
            return Response({"failed": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"failed": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class UserLogin(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request: Request) -> Response:
        try:
            request_serializer = LoginRequestSerializer(data=request.data)
            request_serializer.is_valid(raise_exception=True)
            serializer = UserLoginSerializer(data=request_serializer.data)
            serializer.is_valid(raise_exception=True)
            return Response({"success": serializer.data})
        except ValidationError as e:
            return Response({"failed": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"failed": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class UserLogout(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request: Request) -> Response:
        try:
            request_serializer = LogoutRerquestSerializer(data=request.data)
            request_serializer.is_valid(raise_exception=True)
            refresh_token = request_serializer.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"detail": str(e)})


class UserUpdate(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request: Request) -> Response:
        try:
            request_serializer = UpdateUserRequestSerialiizer(data=request.data)
            request_serializer.is_valid(raise_exception=True)
            user = request.user
            serializer = UserUpdateSerializer(
                instance=user, data=request_serializer.data
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {"success": "User Updated"}, status=status.HTTP_204_NO_CONTENT
            )
        except ValidationError as e:
            return Response({"failed": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"failed": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
