from django.db import models
from django.urls import reverse

from apps.common.models import BaseContentModel, TimeStampedModel


class SiteSettings(TimeStampedModel):
    site_name = models.CharField(max_length=150, default="Beneficent Schools")
    site_tagline = models.CharField(
        max_length=255,
        default="Nurturing Excellence in Western and Islamic Education",
    )
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=50, blank=True)
    whatsapp_number = models.CharField(max_length=50, blank=True)
    address = models.TextField(blank=True)
    logo = models.ImageField(upload_to="branding/", blank=True, null=True)
    favicon = models.ImageField(upload_to="branding/", blank=True, null=True)

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.site_name


class StaticPage(BaseContentModel):
    body = models.TextField()

    class Meta:
        verbose_name = "Static Page"
        verbose_name_plural = "Static Pages"

    def get_absolute_url(self):
        return reverse("core:static_page", kwargs={"slug": self.slug})


class AnnouncementBar(TimeStampedModel):
    message = models.CharField(max_length=255)
    link = models.URLField(blank=True, help_text="Optional link for the announcement")
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Announcement Bar"
        verbose_name_plural = "Announcement Bars"

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        if self.is_active:
            # Only one announcement can be active at a time
            AnnouncementBar.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)


class HomepageHero(TimeStampedModel):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to="hero/")
    primary_button_text = models.CharField(max_length=50, blank=True)
    primary_button_link = models.CharField(max_length=200, blank=True)
    secondary_button_text = models.CharField(max_length=50, blank=True)
    secondary_button_link = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Homepage Hero Slide"
        verbose_name_plural = "Homepage Hero Slides"
        ordering = ["order"]

    def __str__(self):
        return self.title


class FeatureCard(TimeStampedModel):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True, help_text="CSS class for icon (e.g. from FontAwesome)")
    image = models.ImageField(upload_to="features/", blank=True, null=True)
    link = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Feature Card"
        verbose_name_plural = "Feature Cards"
        ordering = ["order"]

    def __str__(self):
        return self.title


class ContactMessage(TimeStampedModel):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Message from {self.name} ({self.created_at.strftime('%Y-%m-%d')})"


class FAQ(TimeStampedModel):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
        ordering = ["order"]

    def __str__(self):
        return self.question