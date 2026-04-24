from django.contrib import admin

from .models import FlightHotelDeal


@admin.register(FlightHotelDeal)
class FlightHotelDealAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'destination_city', 'nights', 'travelers',
        'combined_price', 'savings', 'is_featured', 'slots_available',
    )
    list_filter = ('destination_city', 'is_featured', 'nights')
    search_fields = ('name', 'destination_city', 'description')
    list_editable = ('is_featured',)
    autocomplete_fields = ()
    raw_id_fields = ('flight', 'hotel')
