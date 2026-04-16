from django.db import models
from django.utils import timezone


class PublishedQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(is_published=True).filter(
            models.Q(published_at__isnull=True) | models.Q(published_at__lte=now)
        )

    def featured(self):
        return self.filter(is_featured=True)

    def ordered(self):
        return self.order_by("order", "-published_at", "-created_at", "-id")


PublishedManager = models.Manager.from_queryset(PublishedQuerySet)