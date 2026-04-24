from django.contrib import admin

from .models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'brand', 'category', 'pickup_location',
        'transmission', 'fuel_type', 'seats', 'price_per_day', 'cars_available',
    )
    list_filter = ('category', 'transmission', 'fuel_type', 'pickup_location')
    search_fields = ('name', 'brand', 'pickup_location', 'drop_location')
    ordering = ('category', 'price_per_day')
