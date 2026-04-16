from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from apps.core.sitemaps import (
    StaticViewSitemap, PostSitemap, EventSitemap,
    GallerySitemap, SchoolDivisionSitemap, ProgramPageSitemap
)

sitemaps = {
    "static": StaticViewSitemap,
    "news": PostSitemap,
    "events": EventSitemap,
    "gallery": GallerySitemap,
    "divisions": SchoolDivisionSitemap,
    "programs": ProgramPageSitemap,
}

# Admin Branding
admin.site.site_header = "Beneficent Schools Administration"
admin.site.site_title = "Beneficent Schools Admin Portal"
admin.site.index_title = "Welcome to the School Communications Portal"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("apps.core.urls", "core"), namespace="core")),
    path("academics/", include(("apps.academics.urls", "academics"), namespace="academics")),
    path("admissions/", include(("apps.admissions.urls", "admissions"), namespace="admissions")),
    path("news/", include(("apps.news.urls", "news"), namespace="news")),
    path("events/", include(("apps.events.urls", "events"), namespace="events")),
    path("gallery/", include(("apps.gallery.urls", "gallery"), namespace="gallery")),
    path("downloads/", include(("apps.downloads.urls", "downloads"), namespace="downloads")),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)