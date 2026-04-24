from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Train


def train_list(request):
    qs = Train.objects.all()
    origin = request.GET.get('origin', '').strip()
    destination = request.GET.get('destination', '').strip()
    q = request.GET.get('q', '').strip()
    if origin:
        qs = qs.filter(origin__icontains=origin)
    if destination:
        qs = qs.filter(destination__icontains=destination)
    if q:
        qs = qs.filter(Q(name__icontains=q) | Q(number__icontains=q))
    return render(
        request,
        'trains/train_list.html',
        {'trains': qs, 'origin': origin, 'destination': destination, 'q': q},
    )


def train_detail(request, pk):
    train = get_object_or_404(Train, pk=pk)
    return render(request, 'trains/train_detail.html', {'train': train})
