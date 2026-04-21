from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Flight


def flight_list(request):
    qs = Flight.objects.filter(seats_available__gt=0)
    origin = request.GET.get('origin', '').strip()
    destination = request.GET.get('destination', '').strip()
    if origin:
        qs = qs.filter(origin__icontains=origin)
    if destination:
        qs = qs.filter(destination__icontains=destination)
    q = request.GET.get('q', '').strip()
    if q:
        qs = qs.filter(
            Q(airline__icontains=q)
            | Q(flight_number__icontains=q)
            | Q(origin__icontains=q)
            | Q(destination__icontains=q)
        )
    return render(
        request,
        'flights/flight_list.html',
        {
            'flights': qs,
            'origin': origin,
            'destination': destination,
            'q': q,
        },
    )


def flight_detail(request, pk):
    flight = get_object_or_404(Flight, pk=pk)
    return render(request, 'flights/flight_detail.html', {'flight': flight})
