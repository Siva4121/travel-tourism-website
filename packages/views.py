from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Destination, Package


def package_list(request):
    qs = Package.objects.select_related('destination').all()
    q = request.GET.get('q', '').strip()
    destination = request.GET.get('destination', '').strip()
    if destination:
        qs = qs.filter(
            Q(destination__name__icontains=destination)
            | Q(city__icontains=destination)
        )
    if q:
        qs = qs.filter(
            Q(name__icontains=q)
            | Q(description__icontains=q)
            | Q(destination__name__icontains=q)
            | Q(city__icontains=q)
        )
    destinations = Destination.objects.all()
    return render(
        request,
        'packages/package_list.html',
        {
            'packages': qs,
            'destinations': destinations,
            'q': q,
            'destination': destination,
        },
    )


def package_detail(request, pk):
    package = get_object_or_404(Package, pk=pk)
    return render(request, 'packages/package_detail.html', {'package': package})
