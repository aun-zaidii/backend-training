from django.urls import path

from .views import AggrigationView, StatsView








urlpatterns = [
    path('aggrigation/' , AggrigationView.as_view(),  name= 'agrigation'),
    path('stats/' , StatsView.as_view(),  name= 'stats'),
]
