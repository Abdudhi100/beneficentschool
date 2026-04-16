from django.urls import path
from .views import DownloadListView

app_name = "downloads"

urlpatterns = [
    path("", DownloadListView.as_view(), name="download_list"),
]
