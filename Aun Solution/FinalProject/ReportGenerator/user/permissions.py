from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView

from .enums import RoleChoices


class IsAdmin(BasePermission):
    def has_permission(self, request: Request, view: APIView):
        return request.user.role == RoleChoices.admin


class IsModerator(BasePermission):
    def has_permission(self, request: Request, view: APIView):
        return request.user.role == RoleChoices.moderator


class IsViewer(BasePermission):
    def has_permission(self, request: Request, view: APIView) -> bool:
        return request.user.role == RoleChoices.viewer


class IsAdminOrModeratorOrViewer(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in [
            RoleChoices.admin,
            RoleChoices.moderator,
            RoleChoices.viewer,
        ]


class IsAdminOrModerator(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in [
            RoleChoices.admin,
            RoleChoices.moderator,
        ]
