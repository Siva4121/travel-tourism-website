from django.db import models


class Attraction(models.Model):
    CATEGORY_CHOICES = [
        ('landmark', 'Landmark'),
        ('museum', 'Museum'),
        ('park', 'Park / Nature'),
        ('theme', 'Theme Park'),
        ('tour', 'Guided Tour'),
        ('experience', 'Experience'),
        ('adventure', 'Adventure'),
        ('cruise', 'Cruise'),
        ('water', 'Water Activity'),
    ]

    name = models.CharField(max_length=150)
    city = models.CharField(max_length=80)
    country = models.CharField(max_length=80, default='India')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='experience')
    description = models.TextField(blank=True)
    highlights = models.TextField(
        blank=True,
        help_text='One highlight per line (e.g. Skip-the-line entry, English audio guide)',
    )
    duration_hours = models.DecimalField(max_digits=4, decimal_places=1, default=2, help_text='Estimated duration in hours')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=4.5, help_text='0 - 5')
    reviews_count = models.PositiveIntegerField(default=0)
    slots_available = models.PositiveIntegerField(default=50)
    is_featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='attractions/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-is_featured', '-rating', 'name')

    def __str__(self) -> str:  # pragma: no cover
        return f"{self.name} – {self.city}"

    @property
    def highlight_list(self):
        return [h.strip() for h in self.highlights.splitlines() if h.strip()]
