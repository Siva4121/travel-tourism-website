from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=150)
    city = models.CharField(max_length=80)
    country = models.CharField(max_length=80, default='India')
    address = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    star_rating = models.PositiveSmallIntegerField(default=3)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    rooms_available = models.PositiveIntegerField(default=20)
    amenities = models.CharField(
        max_length=255,
        blank=True,
        help_text='Comma-separated list (e.g. WiFi, Pool, Spa, Gym)',
    )
    image = models.ImageField(upload_to='hotels/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-star_rating', 'name')

    def __str__(self) -> str:  # pragma: no cover
        return f"{self.name} - {self.city}"

    @property
    def amenity_list(self):
        return [a.strip() for a in self.amenities.split(',') if a.strip()]
