from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from user.permissions import (IsAdmin, IsAdminOrModeratorOrViewer, IsModerator,
                              IsViewer)

from .models import CensusLog
from .serializers import CensusLogSerializer
from .service import request_data_for_multiple_years, save_to_db
from .tasks import process_census_data


class DataFetchView(APIView):
    permission_classes = [IsAdmin]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        try:
            years = [
                2010,
                2011,
                2012,
                2013,
                2014,
                2015,
                2016,
                2017,
                2018,
                2019,
                2021,
                2022,
                2023,
            ]
            process_census_data.delay(years)
            return Response({"result": "success"}, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"failed": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"failed": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class StatusLog(APIView):
    permission_classes = [IsAdmin]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        try:
            task_id = "314c38e4-a92f-4907-8640-1237a64cedc3"
            log = CensusLog.objects.get(task_id=task_id)
            serializer = CensusLogSerializer(log)
            return Response({"result": serializer.data}, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"failed": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"failed": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ManualFetchView(APIView):
    permission_classes = [IsAdmin]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        try:
            years = [2021]
            data = request_data_for_multiple_years(years)
            save_to_db(data)
            return Response({"result": "success"}, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"failed": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"failed": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
