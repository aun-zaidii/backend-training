from django.urls import path

from .views import *

urlpatterns = [
    path("fetch/", DataFetchView.as_view(), name="data_fetch"),
    path("statuslog/", StatusLog.as_view(), name="status_log"),
    path("testsave/", TestView.as_view(), name="testsave"),
]
