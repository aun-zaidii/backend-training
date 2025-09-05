from rest_framework.views import APIView
from .helpers import data_aggrigation, statistical_analysis
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response 
from rest_framework import status




class AggrigationView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []
    def post(self, request):
       filters = request.data
       try:
        result = data_aggrigation(filters)
        return Response({'success':result})
       except Exception as e:
          return Response({'failed':str(e)})


class StatsView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []
    def post(self, request):
       filters = request.data
       try:
        result = statistical_analysis(filters)
        return Response({'success':result})
       except Exception as e:
          return Response({'failed':str(e)})
