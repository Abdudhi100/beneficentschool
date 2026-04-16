from django.urls import path
from .views import AcademicsIndexView, SchoolDivisionDetailView, ProgramPageDetailView

app_name = "academics"

urlpatterns = [
    path("", AcademicsIndexView.as_view(), name="index"),
    path("schools/<slug:slug>/", SchoolDivisionDetailView.as_view(), name="division_detail"),
    path("programs/<slug:slug>/", ProgramPageDetailView.as_view(), name="program_detail"),
]
