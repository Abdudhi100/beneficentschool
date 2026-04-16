from django.db import models
from apps.common.models import OrderedModel, PublishableModel

class Testimonial(OrderedModel, PublishableModel):
    """Testimonials for the homepage or dedicated pages."""
    quote = models.TextField()
    author_name = models.CharField(max_length=150)
    author_role = models.CharField(max_length=150, blank=True, help_text="e.g. Parent of Year 4 student")
    image = models.ImageField(upload_to="testimonials/", blank=True, null=True)

    class Meta(OrderedModel.Meta):
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return f"Testimonial from {self.author_name}"
