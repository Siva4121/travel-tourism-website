from django.urls import path

from . import views

urlpatterns = [
    path('', views.booking_list, name='list'),
    path('<int:pk>/', views.booking_detail, name='detail'),
    path('<int:pk>/cancel/', views.cancel_booking, name='cancel'),
    path('flight/<int:flight_id>/', views.book_flight, name='book_flight'),
    path('hotel/<int:hotel_id>/', views.book_hotel, name='book_hotel'),
    path('package/<int:package_id>/', views.book_package, name='book_package'),
]
