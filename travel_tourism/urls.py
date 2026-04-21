from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('core.urls', 'core'), namespace='core')),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('flights/', include(('flights.urls', 'flights'), namespace='flights')),
    path('hotels/', include(('hotels.urls', 'hotels'), namespace='hotels')),
    path('packages/', include(('packages.urls', 'packages'), namespace='packages')),
    path('bookings/', include(('bookings.urls', 'bookings'), namespace='bookings')),
    path('chatbot/', include(('chatbot.urls', 'chatbot'), namespace='chatbot')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "Travel & Tourism Admin"
admin.site.site_title = "Travel & Tourism Admin"
admin.site.index_title = "Administration Dashboard"
