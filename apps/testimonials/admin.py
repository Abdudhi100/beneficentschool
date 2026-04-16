from django.contrib import admin
from .models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("author_name", "author_role", "order", "is_published")
    list_editable = ("order", "is_published")
    search_fields = ("author_name", "quote")
