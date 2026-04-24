from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import FlightHotelDeal


def deal_list(request):
    qs = FlightHotelDeal.objects.all()
    city = request.GET.get('city', '').strip()
    q = request.GET.get('q', '').strip()
    if city:
        qs = qs.filter(destination_city__icontains=city)
    if q:
        qs = qs.filter(
            Q(name__icontains=q)
            | Q(destination_city__icontains=q)
            | Q(description__icontains=q)
        )
    return render(
        request,
        'flighthotel/deal_list.html',
        {'deals': qs, 'city': city, 'q': q},
    )


def deal_detail(request, pk):
    deal = get_object_or_404(FlightHotelDeal, pk=pk)
    return render(request, 'flighthotel/deal_detail.html', {'deal': deal})
