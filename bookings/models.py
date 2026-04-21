from django.conf import settings
from django.db import models

from flights.models import Flight
from hotels.models import Hotel
from packages.models import Package


class Booking(models.Model):
    TYPE_CHOICES = [
        ('flight', 'Flight'),
        ('hotel', 'Hotel'),
        ('package', 'Package'),
    ]
    STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='bookings',
    )
    booking_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    flight = models.ForeignKey(
        Flight, on_delete=models.SET_NULL, null=True, blank=True, related_name='bookings'
    )
    hotel = models.ForeignKey(
        Hotel, on_delete=models.SET_NULL, null=True, blank=True, related_name='bookings'
    )
    package = models.ForeignKey(
        Package, on_delete=models.SET_NULL, null=True, blank=True, related_name='bookings'
    )
    travelers = models.PositiveIntegerField(default=1)
    check_in = models.DateField(null=True, blank=True)
    check_out = models.DateField(null=True, blank=True)
    travel_date = models.DateField(null=True, blank=True)
    total_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='confirmed')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self) -> str:  # pragma: no cover
        return f"Booking #{self.pk} - {self.booking_type} - {self.user.username}"

    @property
    def item_label(self) -> str:
        if self.flight:
            return f"Flight {self.flight.flight_number} ({self.flight.origin}→{self.flight.destination})"
        if self.hotel:
            return f"{self.hotel.name}, {self.hotel.city}"
        if self.package:
            return self.package.name
        return "—"
