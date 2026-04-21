from django.contrib import admin

from .models import Destination, Package


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name', 'country')


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'destination',
        'duration_days',
        'duration_nights',
        'price',
        'slots_available',
        'is_featured',
    )
    list_filter = ('destination', 'is_featured')
    search_fields = ('name', 'city', 'description')
    list_editable = ('is_featured', 'price', 'slots_available')
