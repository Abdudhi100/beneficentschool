from django.db import models
from apps.common.models import OrderedModel, PublishableModel, SluggedModel

class DownloadCategory(OrderedModel, SluggedModel):
    """Categories for downloadable files."""
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta(OrderedModel.Meta):
        verbose_name = "Download Category"
        verbose_name_plural = "Download Categories"

    def __str__(self):
        return self.title

class Download(OrderedModel, PublishableModel):
    """A downloadable file."""
    category = models.ForeignKey(DownloadCategory, on_delete=models.CASCADE, related_name="downloads")
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to="downloads/")

    class Meta(OrderedModel.Meta):
        verbose_name = "Download"
        verbose_name_plural = "Downloads"

    def __str__(self):
        return self.title
