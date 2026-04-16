from django.db import models
from django.urls import reverse
from apps.common.models import BaseContentModel, OrderedModel

class SchoolDivision(BaseContentModel):
    """E.g., Primary School, Secondary School"""
    overview = models.TextField(blank=True)
    teaching_approach = models.TextField(blank=True)
    image = models.ImageField(upload_to="divisions/", blank=True, null=True)

    class Meta:
        verbose_name = "School Division"
        verbose_name_plural = "School Divisions"

    def get_absolute_url(self):
        return reverse("academics:division_detail", kwargs={"slug": self.slug})


class ProgramPage(BaseContentModel):
    """E.g., Western Education, Islamic Education"""
    overview = models.TextField(blank=True)
    curriculum_details = models.TextField(blank=True)
    image = models.ImageField(upload_to="programs/", blank=True, null=True)

    class Meta:
        verbose_name = "Program Page"
        verbose_name_plural = "Program Pages"

    def get_absolute_url(self):
        return reverse("academics:program_detail", kwargs={"slug": self.slug})


class SubjectArea(OrderedModel):
    """E.g., Numeracy, Literacy, Qur'an Studies"""
    program = models.ForeignKey(ProgramPage, on_delete=models.CASCADE, related_name="subjects", null=True, blank=True)
    division = models.ForeignKey(SchoolDivision, on_delete=models.CASCADE, related_name="subjects", null=True, blank=True)
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True, help_text="CSS class for icon")

    class Meta(OrderedModel.Meta):
        verbose_name = "Subject Area"
        verbose_name_plural = "Subject Areas"

    def __str__(self):
        parent = f" ({self.program.title})" if self.program else (f" ({self.division.title})" if self.division else "")
        return f"{self.name}{parent}"
