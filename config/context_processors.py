from apps.core.models import SiteSettings, AnnouncementBar


def site_context(request):
    settings_obj = SiteSettings.objects.first()
    announcement = AnnouncementBar.objects.filter(is_active=True).first()

    return {
        "site_name": getattr(settings_obj, "site_name", "Beneficent Schools"),
        "school_tagline": getattr(
            settings_obj,
            "site_tagline",
            "Nurturing Excellence in Western and Islamic Education",
        ),
        "site_settings": settings_obj,
        "announcement": announcement,
    }