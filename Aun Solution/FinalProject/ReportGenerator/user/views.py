from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import *


class UserRegistrationView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request: Request) -> Response:
        try:
            data = request.data
            serializer = UserRegistrationSerializer(data=data)
            serializer.is_valid()
            serializer.save()
            send_mail(
                "Registeration MAil",
                "You are registered successfully",
                "aun.zaidi@evolvyxlabs.com",
                [data["email"]],
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
            serializer = UserLoginSerializer(data=request.data)
            serializer.is_valid()
            return Response({"success": serializer.data})
        except ValidationError as e:
            return Response({"failed": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"failed": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class UserLogout(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request: Request) -> Response:
        try:
            refresh_token = request.data["refresh_token"]
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
            data = request.data
            user = request.user
            serializer = UserUpdateSerializer(instance=user, data=data)
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
