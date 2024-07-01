from django.urls import path

from . import views

urlpatterns = [
    path('hello/', views.WeatherView.as_view(), name='hello'),
]