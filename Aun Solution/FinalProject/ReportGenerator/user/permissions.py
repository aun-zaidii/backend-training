from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView

class IsAdmin(BasePermission):
    def has_permission(self, request:Request, view:APIView):
        return request.user.role == "admin"

class IsModerator(BasePermission):
    def has_permission(self, request:Request, view:APIView):
        return request.user.role == "moderator" 

class IsViewer(BasePermission):
    def has_permission(self, request:Request, view:APIView) ->bool:
        return request.user.role == "viewer" 