from django.shortcuts import render

from attractions.models import Attraction
from cars.models import Car
from flighthotel.models import FlightHotelDeal
from flights.models import Flight
from hotels.models import Hotel
from packages.models import Destination, Package
from trains.models import Train


def home(request):
    featured_packages = Package.objects.filter(is_featured=True)[:6]
    if not featured_packages.exists():
        featured_packages = Package.objects.all()[:6]

    featured_attractions = Attraction.objects.filter(is_featured=True)[:4]
    if not featured_attractions.exists():
        featured_attractions = Attraction.objects.all()[:4]

    featured_deals = FlightHotelDeal.objects.filter(is_featured=True)[:4]
    if not featured_deals.exists():
        featured_deals = FlightHotelDeal.objects.all()[:4]

    context = {
        'destinations': Destination.objects.all()[:8],
        'featured_packages': featured_packages,
        'top_hotels': Hotel.objects.order_by('-star_rating')[:6],
        'upcoming_flights': Flight.objects.filter(seats_available__gt=0)[:4],
        'upcoming_trains': Train.objects.all()[:4],
        'featured_cars': Car.objects.all()[:4],
        'featured_attractions': featured_attractions,
        'featured_deals': featured_deals,
    }
    return render(request, 'core/home.html', context)


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')
