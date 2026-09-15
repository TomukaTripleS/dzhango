from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_place),
    path('', views.place_list),
    path('<int:id>/', views.place_detail),
]
