from django.contrib import admin
from .models import GalleryAlbum, GalleryImage

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 3

@admin.register(GalleryAlbum)
class GalleryAlbumAdmin(admin.ModelAdmin):
    list_display = ("title", "date_taken", "is_published")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [GalleryImageInline]
