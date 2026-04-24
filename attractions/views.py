from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Attraction


def attraction_list(request):
    qs = Attraction.objects.all()
    city = request.GET.get('city', '').strip()
    category = request.GET.get('category', '').strip()
    q = request.GET.get('q', '').strip()
    if city:
        qs = qs.filter(city__icontains=city)
    if category:
        qs = qs.filter(category=category)
    if q:
        qs = qs.filter(
            Q(name__icontains=q)
            | Q(city__icontains=q)
            | Q(description__icontains=q)
        )
    return render(
        request,
        'attractions/attraction_list.html',
        {
            'attractions': qs,
            'city': city,
            'category': category,
            'q': q,
            'categories': Attraction.CATEGORY_CHOICES,
        },
    )


def attraction_detail(request, pk):
    attraction = get_object_or_404(Attraction, pk=pk)
    return render(
        request,
        'attractions/attraction_detail.html',
        {'attraction': attraction},
    )
