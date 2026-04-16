from django.urls import path
from .views import AdmissionsIndexView

app_name = "admissions"

urlpatterns = [
    path("", AdmissionsIndexView.as_view(), name="index"),
]
