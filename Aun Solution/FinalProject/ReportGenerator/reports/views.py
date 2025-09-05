from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .helpers import *


class CensusReportView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        data = request.data
        try:
            response = generate_county_report(data)
            return response
        except Exception as e:
            return Response({"failed": str(e)})


class DetailReportView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        data = request.data
        try:
            response = generate_county_report(data)
            return response
        except Exception as e:
            return Response({"failed": str(e)})
