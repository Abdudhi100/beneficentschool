from django.db import models
from django.urls import reverse
from apps.common.models import BaseContentModel

class Event(BaseContentModel):
    """Upcoming or past events."""
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to="events/", blank=True, null=True)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ["start_date"]

    def get_absolute_url(self):
        return reverse("events:event_detail", kwargs={"slug": self.slug})
