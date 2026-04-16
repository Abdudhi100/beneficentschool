from django.views.generic import ListView, DetailView
from .models import GalleryAlbum

class AlbumListView(ListView):
    model = GalleryAlbum
    template_name = "gallery/album_list.html"
    context_object_name = "albums"
    paginate_by = 12

    def get_queryset(self):
        return GalleryAlbum.objects.filter(is_published=True)

class AlbumDetailView(DetailView):
    model = GalleryAlbum
    template_name = "gallery/album_detail.html"
    context_object_name = "album"

    def get_queryset(self):
        return GalleryAlbum.objects.filter(is_published=True)
