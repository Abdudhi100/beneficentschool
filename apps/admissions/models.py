from django.db import models
from apps.common.models import BaseContentModel, OrderedModel, TimeStampedModel

class AdmissionPage(BaseContentModel):
    """Singleton-like model for the Admissions Landing Page Content."""
    intro_text = models.TextField(blank=True, help_text="Welcome text for the admissions page.")
    fee_notes = models.TextField(blank=True, help_text="Information about fees or how to request a fee schedule.")
    contact_notes = models.TextField(blank=True, help_text="Extra contact info or office hours.")

    class Meta:
        verbose_name = "Admission Page Content"
        verbose_name_plural = "Admission Page Content"


class AdmissionStep(OrderedModel):
    """Steps in the application process."""
    title = models.CharField(max_length=150)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True, help_text="CSS class for icon")
    is_active = models.BooleanField(default=True)

    class Meta(OrderedModel.Meta):
        verbose_name = "Admission Step"
        verbose_name_plural = "Admission Steps"

    def __str__(self):
        return f"{self.order}. {self.title}"


class AdmissionRequirement(OrderedModel):
    """Documents or criteria required for admission."""
    item = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta(OrderedModel.Meta):
        verbose_name = "Admission Requirement"
        verbose_name_plural = "Admission Requirements"

    def __str__(self):
        return self.item


class AdmissionFAQ(OrderedModel):
    """FAQs specifically for admissions."""
    question = models.CharField(max_length=255)
    answer = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta(OrderedModel.Meta):
        verbose_name = "Admission FAQ"
        verbose_name_plural = "Admission FAQs"

    def __str__(self):
        return self.question


class AdmissionInquiry(TimeStampedModel):
    """Lead capture from the admissions enquiry form."""
    parent_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    child_name = models.CharField(max_length=150)
    child_age = models.PositiveIntegerField()
    class_applied_for = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    is_reviewed = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Admission Inquiry"
        verbose_name_plural = "Admission Inquiries"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Inquiry from {self.parent_name} for {self.child_name}"
