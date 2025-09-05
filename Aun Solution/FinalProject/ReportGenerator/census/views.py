from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .service import *
from .tasks import *

from .serializers import CensusLogSerializer


class DataFetchView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def get(self, request):
        try:
            years = [2017, 2018]
            result = process_census_data.delay(years)
            return Response({"result": "success"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"failed": str(e)})


class StatusLog(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def get(self, request):
        try:
            task_id = "314c38e4-a92f-4907-8640-1237a64cedc3"
            log = CensusLog.objects.get(task_id=task_id)
            serializer = CensusLogSerializer(log)
            return Response({"result": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"failed": str(e)})


class TestView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def get(self, request):
        try:
            years = [2010, 2014]
            data = request_data_for_multiple_years(years)
            result = save_to_db(data)
            return Response({"result": "success"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"failed": str(e)})
