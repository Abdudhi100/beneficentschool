from django.contrib import admin
from .models import DownloadCategory, Download

@admin.register(DownloadCategory)
class DownloadCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "order")
    list_editable = ("order",)
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Download)
class DownloadAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "order", "is_published")
    list_editable = ("order", "is_published")
    list_filter = ("category", "is_published")
    search_fields = ("title", "description")
