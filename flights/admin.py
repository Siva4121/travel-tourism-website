from django.contrib import admin

from .models import Flight


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = (
        'flight_number',
        'airline',
        'origin',
        'destination',
        'departure',
        'arrival',
        'travel_class',
        'price',
        'seats_available',
    )
    list_filter = ('airline', 'travel_class', 'origin', 'destination')
    search_fields = ('flight_number', 'airline', 'origin', 'destination')
    date_hierarchy = 'departure'
