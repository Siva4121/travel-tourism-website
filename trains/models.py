from django.db import models


class Train(models.Model):
    CLASS_CHOICES = [
        ('SL', 'Sleeper'),
        ('3A', 'AC 3-Tier'),
        ('2A', 'AC 2-Tier'),
        ('1A', 'AC First Class'),
        ('CC', 'Chair Car'),
        ('EC', 'Executive Chair Car'),
    ]

    name = models.CharField(max_length=120)
    number = models.CharField(max_length=10, unique=True)
    origin = models.CharField(max_length=80)
    destination = models.CharField(max_length=80)
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    travel_class = models.CharField(max_length=2, choices=CLASS_CHOICES, default='SL')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seats_available = models.PositiveIntegerField(default=100)
    image = models.ImageField(upload_to='trains/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('departure',)

    def __str__(self) -> str:  # pragma: no cover
        return f"{self.name} ({self.number}) {self.origin}→{self.destination}"

    @property
    def duration_hours(self) -> float:
        delta = self.arrival - self.departure
        return round(delta.total_seconds() / 3600, 1)
