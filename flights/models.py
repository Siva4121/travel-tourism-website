from django.db import models


class Flight(models.Model):
    CLASS_CHOICES = [
        ('economy', 'Economy'),
        ('premium', 'Premium Economy'),
        ('business', 'Business'),
        ('first', 'First Class'),
    ]

    airline = models.CharField(max_length=80)
    flight_number = models.CharField(max_length=20, unique=True)
    origin = models.CharField(max_length=80)
    destination = models.CharField(max_length=80)
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    travel_class = models.CharField(max_length=20, choices=CLASS_CHOICES, default='economy')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seats_available = models.PositiveIntegerField(default=50)
    image = models.ImageField(upload_to='flights/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('departure',)

    def __str__(self) -> str:  # pragma: no cover
        return f"{self.airline} {self.flight_number} ({self.origin}→{self.destination})"
