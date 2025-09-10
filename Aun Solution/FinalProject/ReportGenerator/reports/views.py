from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from user.permissions import (IsAdmin, IsAdminOrModerator,
                              IsAdminOrModeratorOrViewer, IsModerator,
                              IsViewer)

from .helpers import generate_county_report, generate_detail_report
from .serializers import (CountyReportRequestSerializer,
                          DetailReportRequestSerializer,
                          DetailResponseSerializer)


class CountyReportView(APIView):
    permission_classes = [IsAdminOrModeratorOrViewer]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            request_serializer = CountyReportRequestSerializer(data=request.data)
            request_serializer.is_valid(raise_exception=True)
            response = generate_county_report(request_serializer.data)
            return response
        except Exception as e:
            return Response({"failed": str(e)})


class DetailReportView(APIView):
    permission_classes = [IsAdminOrModeratorOrViewer]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            data = request.data
            request_serializer = DetailReportRequestSerializer(data=request.data)
            request_serializer.is_valid(raise_exception=True)
            response = generate_detail_report(request_serializer.data)
            return response
        except Exception as e:
            return Response({"failed": str(e)})
