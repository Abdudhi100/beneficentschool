from django.contrib import admin
from .models import SchoolDivision, ProgramPage, SubjectArea

class SubjectAreaInline(admin.TabularInline):
    model = SubjectArea
    extra = 1

@admin.register(SchoolDivision)
class SchoolDivisionAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "is_published")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [SubjectAreaInline]

@admin.register(ProgramPage)
class ProgramPageAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "is_published")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [SubjectAreaInline]

@admin.register(SubjectArea)
class SubjectAreaAdmin(admin.ModelAdmin):
    list_display = ("name", "program", "division", "order")
    list_editable = ("order",)
    list_filter = ("program", "division")
