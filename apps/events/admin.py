from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "start_date", "is_published")
    list_filter = ("is_published", "start_date")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "description", "location")
