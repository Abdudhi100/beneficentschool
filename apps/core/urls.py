from django.urls import path

from .views import HomeView, StaticPageDetailView, AboutView, FAQListView, ContactView

app_name = "core"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("faq/", FAQListView.as_view(), name="faq"),
    path("pages/<slug:slug>/", StaticPageDetailView.as_view(), name="static_page"),
]