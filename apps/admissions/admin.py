from django.contrib import admin
from .models import AdmissionPage, AdmissionStep, AdmissionRequirement, AdmissionFAQ, AdmissionInquiry

@admin.register(AdmissionPage)
class AdmissionPageAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published")
    prepopulated_fields = {"slug": ("title",)}

@admin.register(AdmissionStep)
class AdmissionStepAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active")
    list_editable = ("order", "is_active")

@admin.register(AdmissionRequirement)
class AdmissionRequirementAdmin(admin.ModelAdmin):
    list_display = ("item", "order", "is_active")
    list_editable = ("order", "is_active")

@admin.register(AdmissionFAQ)
class AdmissionFAQAdmin(admin.ModelAdmin):
    list_display = ("question", "order", "is_active")
    list_editable = ("order", "is_active")

@admin.register(AdmissionInquiry)
class AdmissionInquiryAdmin(admin.ModelAdmin):
    list_display = ("parent_name", "child_name", "class_applied_for", "created_at", "is_reviewed")
    list_filter = ("is_reviewed", "class_applied_for", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("parent_name", "email", "phone", "child_name")
