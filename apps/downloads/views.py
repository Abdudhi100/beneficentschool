from django.views.generic import ListView
from .models import DownloadCategory, Download

class DownloadListView(ListView):
    model = DownloadCategory
    template_name = "downloads/download_list.html"
    context_object_name = "categories"

    def get_queryset(self):
        return DownloadCategory.objects.prefetch_related("downloads").all()
