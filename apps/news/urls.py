from django.urls import path
from .views import PostListView, PostDetailView

app_name = "news"

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
]
