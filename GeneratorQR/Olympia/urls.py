from django.urls import path
from . import views

urlpatterns = [
    path('', views.lang),
    #path('/', views.lang),
    path('en/', views.home_en),
    path('by/', views.home_by),
    #path('/en/', views.home)
    #path('code/', views.code)
]
