from django.db import models
from django.urls import reverse
from apps.common.models import BaseContentModel, SluggedModel

class Category(SluggedModel):
    """Categories for news classification."""
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Post(BaseContentModel):
    """News or Blog Post."""
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="posts")
    excerpt = models.TextField(blank=True, help_text="Short summary for lists.")
    content = models.TextField()
    image = models.ImageField(upload_to="news/", blank=True, null=True)
    author = models.CharField(max_length=150, blank=True)
    publish_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "News Post"
        verbose_name_plural = "News Posts"
        ordering = ["-publish_date", "-created_at"]

    def get_absolute_url(self):
        return reverse("news:post_detail", kwargs={"slug": self.slug})
