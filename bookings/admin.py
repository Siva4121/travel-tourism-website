from django.contrib import admin

from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'booking_type',
        'item_label',
        'travelers',
        'total_price',
        'status',
        'created_at',
    )
    list_filter = ('booking_type', 'status', 'created_at')
    search_fields = ('user__username', 'user__email')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)
