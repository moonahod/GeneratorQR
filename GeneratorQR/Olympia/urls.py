from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('guide/', views.guide),
    path('start/', views.start),
    path('code/', views.code)
]