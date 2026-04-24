from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Car


def car_list(request):
    qs = Car.objects.all()
    location = request.GET.get('location', '').strip()
    category = request.GET.get('category', '').strip()
    q = request.GET.get('q', '').strip()
    if location:
        qs = qs.filter(Q(pickup_location__icontains=location) | Q(drop_location__icontains=location))
    if category:
        qs = qs.filter(category=category)
    if q:
        qs = qs.filter(Q(name__icontains=q) | Q(brand__icontains=q) | Q(description__icontains=q))
    return render(
        request,
        'cars/car_list.html',
        {
            'cars': qs,
            'location': location,
            'category': category,
            'q': q,
            'categories': Car.CATEGORY_CHOICES,
        },
    )


def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'cars/car_detail.html', {'car': car})
