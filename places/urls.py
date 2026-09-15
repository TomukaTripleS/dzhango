from django.urls import path, include
from . import views

urlpatterns = [
    path('add/', views),
    path('', views),
    path('<int:id>/', views),
]
