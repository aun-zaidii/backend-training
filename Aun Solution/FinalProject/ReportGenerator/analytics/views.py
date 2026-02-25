from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from user.permissions import (IsAdmin, IsAdminOrModerator,
                              IsAdminOrModeratorOrViewer, IsModerator,
                              IsViewer)

from .helpers import (data_aggrigation, statistical_analysis,
                      time_based_analysis)
from .serializers import (AggregationResponseSerializer,
                          AggregationStatsRequestSerializer,
                          StatisticalAnalysisResponseSerializer,
                          TimeBaseRequestSerializer)


class AggrigationView(APIView):
    permission_classes = [IsAdmin]
    authentication_classes = [JWTAuthentication]

    def post(self, request) -> Response:
        try:
            request_serializer = AggregationStatsRequestSerializer(data=request.data)
            request_serializer.is_valid(raise_exception=True)
            result = data_aggrigation(request_serializer.data)
            response_serializer = AggregationResponseSerializer(instance=result)
            final_result = response_serializer.data
            return Response({"success": final_result})
        except ValidationError as e:
            return Response({"failed": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"failed": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class StatsView(APIView):
    permission_classes = [IsAdminOrModerator]
    authentication_classes = [JWTAuthentication]

    def post(self, request) -> Response:
        try:
            serializer = AggregationStatsRequestSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            filters = serializer.data
            result = statistical_analysis(filters)
            response_serializer = StatisticalAnalysisResponseSerializer(instance=result)
            final_result = response_serializer.data
            return Response({"success": final_result})
        except ValidationError as e:
            return Response({"failed": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"failed": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class TimeBaseAnalytics(APIView):
    permission_classes = [IsAdminOrModerator]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            serializer = TimeBaseRequestSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            result = time_based_analysis(serializer.data)
            return Response(result)
        except ValidationError as e:
            return Response({"failed": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"failed": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
