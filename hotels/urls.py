from django.urls import path

from . import views

urlpatterns = [
    path('', views.hotel_list, name='list'),
    path('<int:pk>/', views.hotel_detail, name='detail'),
]
