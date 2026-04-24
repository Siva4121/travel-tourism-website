from django.urls import path

from . import views

urlpatterns = [
    path('', views.deal_list, name='list'),
    path('<int:pk>/', views.deal_detail, name='detail'),
]
