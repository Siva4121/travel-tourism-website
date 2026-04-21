from django.shortcuts import render

from flights.models import Flight
from hotels.models import Hotel
from packages.models import Destination, Package


def home(request):
    featured_packages = Package.objects.filter(is_featured=True)[:6]
    if not featured_packages.exists():
        featured_packages = Package.objects.all()[:6]
    context = {
        'destinations': Destination.objects.all()[:8],
        'featured_packages': featured_packages,
        'top_hotels': Hotel.objects.order_by('-star_rating')[:4],
        'upcoming_flights': Flight.objects.filter(seats_available__gt=0)[:4],
    }
    return render(request, 'core/home.html', context)


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')
