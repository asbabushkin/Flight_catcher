from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from flight_search.views import pageNotFound

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("flight_search.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = pageNotFound
