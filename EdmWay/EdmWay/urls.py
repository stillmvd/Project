from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('site_display.urls')),
    path('account/', include('site_display.urls')),
    path('authorization/', include('site_display.urls')),
    path('performers/', include('site_display.urls')),
    path('registration/', include('site_display.urls')),
    path('genres/', include('site_display.urls')),
]
