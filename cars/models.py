from django.db import models


class Car(models.Model):
    CATEGORY_CHOICES = [
        ('economy', 'Economy'),
        ('compact', 'Compact'),
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('luxury', 'Luxury'),
        ('van', 'Van / MPV'),
    ]
    TRANSMISSION_CHOICES = [
        ('manual', 'Manual'),
        ('automatic', 'Automatic'),
    ]
    FUEL_CHOICES = [
        ('petrol', 'Petrol'),
        ('diesel', 'Diesel'),
        ('electric', 'Electric'),
        ('hybrid', 'Hybrid'),
    ]

    name = models.CharField(max_length=120, help_text='e.g. Toyota Innova Crysta')
    brand = models.CharField(max_length=80, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='sedan')
    pickup_location = models.CharField(max_length=120)
    drop_location = models.CharField(max_length=120, blank=True)
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_CHOICES, default='manual')
    fuel_type = models.CharField(max_length=20, choices=FUEL_CHOICES, default='petrol')
    seats = models.PositiveSmallIntegerField(default=5)
    luggage_capacity = models.PositiveSmallIntegerField(default=2, help_text='Number of large bags')
    air_conditioning = models.BooleanField(default=True)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    cars_available = models.PositiveIntegerField(default=10)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='cars/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('category', 'price_per_day')

    def __str__(self) -> str:  # pragma: no cover
        return f"{self.name} ({self.get_category_display()})"
