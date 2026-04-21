from django.contrib import admin

from .models import Hotel


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'country', 'star_rating', 'price_per_night', 'rooms_available')
    list_filter = ('city', 'star_rating', 'country')
    search_fields = ('name', 'city', 'address', 'amenities')
