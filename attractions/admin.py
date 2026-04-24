from django.contrib import admin

from .models import Attraction


@admin.register(Attraction)
class AttractionAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'city', 'country', 'category', 'duration_hours',
        'price', 'rating', 'reviews_count', 'is_featured',
    )
    list_filter = ('category', 'city', 'country', 'is_featured')
    search_fields = ('name', 'city', 'description', 'highlights')
    list_editable = ('is_featured',)
    ordering = ('-is_featured', '-rating')
