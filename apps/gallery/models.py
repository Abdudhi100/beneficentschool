from django.db import models
from django.urls import reverse
from apps.common.models import BaseContentModel, OrderedModel

class GalleryAlbum(BaseContentModel):
    """A collection of images."""
    description = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to="gallery/covers/")
    date_taken = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = "Gallery Album"
        verbose_name_plural = "Gallery Albums"
        ordering = ["-date_taken", "-created_at"]

    def get_absolute_url(self):
        return reverse("gallery:album_detail", kwargs={"slug": self.slug})

class GalleryImage(OrderedModel):
    """An individual image in an album."""
    album = models.ForeignKey(GalleryAlbum, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="gallery/images/")
    caption = models.CharField(max_length=255, blank=True)

    class Meta(OrderedModel.Meta):
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"

    def __str__(self):
        return f"Image in {self.album.title}"
