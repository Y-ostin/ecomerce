from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from django.contrib import admin


urlpatterns = [
                  path('users/', include('users.urls')),
                  path('admin/', admin.site.urls), 
                  path('shop/', include('store.urls')),
                  path('', RedirectView.as_view(pattern_name='home', permanent=False))

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
