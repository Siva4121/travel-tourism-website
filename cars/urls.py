from django.urls import path

from . import views

urlpatterns = [
    path('', views.car_list, name='list'),
    path('<int:pk>/', views.car_detail, name='detail'),
]
