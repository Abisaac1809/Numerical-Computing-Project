from django.urls import path
from Apps.DataVisualization.views import data_visualization_views

urlpatterns = [
    path("randomGraph/", data_visualization_views, name="getRandomGraphAndPoints"),
]
