from django.urls import path

from . import views

urlpatterns = [
    path('', views.train_list, name='list'),
    path('<int:pk>/', views.train_detail, name='detail'),
]
