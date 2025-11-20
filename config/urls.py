from django.contrib import admin
from django.urls import re_path, include

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView
)

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    re_path("api/places/", include('places.urls')),
    re_path("api/player/", include('player.urls')),
    re_path("", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]
