from django.db.utils import OperationalError, ProgrammingError
from apps.core.models import SiteSettings, AnnouncementBar


def site_context(request):
    settings_obj = None
    announcement = None

    try:
        settings_obj = SiteSettings.objects.first()
        announcement = AnnouncementBar.objects.filter(is_active=True).first()
    except (OperationalError, ProgrammingError):
        pass

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