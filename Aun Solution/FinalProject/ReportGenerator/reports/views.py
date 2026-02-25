from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from user.permissions import (IsAdmin, IsAdminOrModerator,
                              IsAdminOrModeratorOrViewer, IsModerator,
                              IsViewer)

from .helpers import (county_report_csv, county_report_json, detail_report_csv,
                      detail_report_json)
from .serializers import (CountyReportRequestSerializer,
                          CountyReportResponseSerializer,
                          DetailReportRequestSerializer,
                          DetailReportResponseSerializer)


class CountyReportCsvView(APIView):
    permission_classes = [IsAdminOrModeratorOrViewer]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            request_serializer = CountyReportRequestSerializer(data=request.data)
            request_serializer.is_valid(raise_exception=True)
            response = county_report_csv(request_serializer.data)
            return response
        except ValidationError as e:
            return Response({"failed": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"failed": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class CountyReportJsonView(APIView):
    permission_classes = [IsAdminOrModeratorOrViewer]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            request_serializer = CountyReportRequestSerializer(data=request.data)
            request_serializer.is_valid(raise_exception=True)
            response = county_report_json(request_serializer.data)
            response_serializer = CountyReportResponseSerializer(
                instance=response, many=True
            )
            return Response(
                {"result": response_serializer.data}, status=status.HTTP_200_OK
            )
        except ValidationError as e:
            return Response({"failed": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"failed": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class DetailReportCsvView(APIView):
    permission_classes = [IsAdminOrModeratorOrViewer]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            request_serializer = DetailReportRequestSerializer(data=request.data)
            request_serializer.is_valid(raise_exception=True)
            response = detail_report_csv(request_serializer.data)
            return response
        except ValidationError as e:
            return Response({"failed": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"failed": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class DetailReportJsonView(APIView):
    permission_classes = [IsAdminOrModeratorOrViewer]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            request_serializer = DetailReportRequestSerializer(data=request.data)
            request_serializer.is_valid(raise_exception=True)
            response = detail_report_json(request_serializer.data)
            breakpoint()
            response_serializer = DetailReportResponseSerializer(
                instance=response, many=True
            )
            return Response({"result": response_serializer.data})
        except ValidationError as e:
            return Response({"failed": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"failed": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
