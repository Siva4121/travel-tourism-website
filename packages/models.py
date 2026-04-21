from django.db import models


class Destination(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=80, default='India')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='destinations/', blank=True, null=True)

    class Meta:
        ordering = ('name',)

    def __str__(self) -> str:  # pragma: no cover
        return self.name


class Package(models.Model):
    name = models.CharField(max_length=150)
    destination = models.ForeignKey(
        Destination,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='packages',
    )
    city = models.CharField(max_length=80, blank=True)
    duration_days = models.PositiveIntegerField(default=3)
    duration_nights = models.PositiveIntegerField(default=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    includes = models.TextField(
        blank=True,
        help_text='One item per line (e.g. Hotel stay, Breakfast, Airport transfer)',
    )
    description = models.TextField(blank=True)
    itinerary = models.TextField(
        blank=True,
        help_text='Day-wise itinerary. One day per line.',
    )
    image = models.ImageField(upload_to='packages/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    slots_available = models.PositiveIntegerField(default=30)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-is_featured', '-created_at')

    def __str__(self) -> str:  # pragma: no cover
        return self.name

    @property
    def duration_label(self) -> str:
        return f"{self.duration_nights}N / {self.duration_days}D"

    @property
    def include_list(self):
        return [i.strip() for i in self.includes.splitlines() if i.strip()]

    @property
    def itinerary_list(self):
        return [i.strip() for i in self.itinerary.splitlines() if i.strip()]
