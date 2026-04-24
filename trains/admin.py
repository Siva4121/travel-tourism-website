from django.contrib import admin

from .models import Train


@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = (
        'number', 'name', 'origin', 'destination',
        'departure', 'arrival', 'travel_class', 'price', 'seats_available',
    )
    list_filter = ('travel_class', 'origin', 'destination')
    search_fields = ('name', 'number', 'origin', 'destination')
    date_hierarchy = 'departure'
    ordering = ('departure',)
