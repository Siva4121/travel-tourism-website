from django.db import models

from flights.models import Flight
from hotels.models import Hotel


class FlightHotelDeal(models.Model):
    name = models.CharField(max_length=150, help_text='e.g. Mumbai → Goa: 3N Beachfront Combo')
    destination_city = models.CharField(max_length=80)
    flight = models.ForeignKey(
        Flight,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='combo_deals',
    )
    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='combo_deals',
    )
    nights = models.PositiveIntegerField(default=3)
    travelers = models.PositiveIntegerField(default=2)
    combined_price = models.DecimalField(max_digits=10, decimal_places=2)
    savings = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        help_text='Amount saved vs booking separately',
    )
    description = models.TextField(blank=True)
    inclusions = models.TextField(
        blank=True,
        help_text='One inclusion per line (e.g. Round-trip flight, 3 nights hotel, Daily breakfast)',
    )
    is_featured = models.BooleanField(default=False)
    slots_available = models.PositiveIntegerField(default=20)
    image = models.ImageField(upload_to='flighthotel/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-is_featured', '-created_at')

    def __str__(self) -> str:  # pragma: no cover
        return self.name

    @property
    def inclusion_list(self):
        return [i.strip() for i in self.inclusions.splitlines() if i.strip()]
