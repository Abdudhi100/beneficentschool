from django.contrib import admin
from .models import Category, Post

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_published", "publish_date")
    list_filter = ("is_published", "category", "publish_date")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "content")
