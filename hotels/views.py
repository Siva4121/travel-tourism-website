from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Hotel


def hotel_list(request):
    qs = Hotel.objects.all()
    city = request.GET.get('city', '').strip()
    q = request.GET.get('q', '').strip()
    if city:
        qs = qs.filter(city__icontains=city)
    if q:
        qs = qs.filter(
            Q(name__icontains=q)
            | Q(city__icontains=q)
            | Q(description__icontains=q)
        )
    return render(
        request,
        'hotels/hotel_list.html',
        {'hotels': qs, 'city': city, 'q': q},
    )


def hotel_detail(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    return render(request, 'hotels/hotel_detail.html', {'hotel': hotel})
