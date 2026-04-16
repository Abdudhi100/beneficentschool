from django.db import models
from django.utils import timezone

from .managers import PublishedManager
from .utils import generate_unique_slug


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class OrderedModel(models.Model):
    order = models.PositiveIntegerField(default=0, db_index=True)

    class Meta:
        abstract = True
        ordering = ["order", "id"]


class PublishableModel(models.Model):
    is_published = models.BooleanField(default=True, db_index=True)
    published_at = models.DateTimeField(blank=True, null=True)
    is_featured = models.BooleanField(default=False, db_index=True)

    objects = PublishedManager()

    class Meta:
        abstract = True

    @property
    def is_live(self):
        if not self.is_published:
            return False
        if self.published_at is None:
            return True
        return self.published_at <= timezone.now()


class SluggedModel(models.Model):
    slug = models.SlugField(max_length=220, unique=True, blank=True)

    class Meta:
        abstract = True

    def get_slug_source(self):
        return getattr(self, "title", None) or getattr(self, "name", None)

    def save(self, *args, **kwargs):
        if not self.slug:
            source = self.get_slug_source()
            if source:
                self.slug = generate_unique_slug(self, source)
        super().save(*args, **kwargs)


class SEOModel(models.Model):
    meta_title = models.CharField(max_length=255, blank=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.CharField(max_length=500, blank=True)
    canonical_url = models.URLField(blank=True)
    og_title = models.CharField(max_length=255, blank=True)
    og_description = models.TextField(blank=True)
    og_image = models.ImageField(upload_to="seo/og/", blank=True, null=True)
    robots = models.CharField(max_length=100, default="index,follow")

    class Meta:
        abstract = True

    def get_meta_title(self):
        return self.meta_title or getattr(self, "title", "") or getattr(self, "name", "")

    def get_meta_description(self):
        return self.meta_description or getattr(self, "summary", "") or ""

    def get_og_title(self):
        return self.og_title or self.get_meta_title()

    def get_og_description(self):
        return self.og_description or self.get_meta_description()


class BaseContentModel(
    TimeStampedModel,
    OrderedModel,
    PublishableModel,
    SluggedModel,
    SEOModel,
):
    title = models.CharField(max_length=220)
    summary = models.TextField(blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title