from django.contrib.sitemaps import Sitemap
from apps.core.models import StaticPage
from apps.news.models import Post
from apps.events.models import Event
from apps.gallery.models import GalleryAlbum
from apps.academics.models import SchoolDivision, ProgramPage

class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = "weekly"

    def items(self):
        return StaticPage.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at

class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Post.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at

class EventSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Event.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at

class GallerySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return GalleryAlbum.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at

class SchoolDivisionSitemap(Sitemap):
    priority = 0.9
    changefreq = "monthly"

    def items(self):
        return SchoolDivision.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at

class ProgramPageSitemap(Sitemap):
    priority = 0.9
    changefreq = "monthly"

    def items(self):
        return ProgramPage.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at
