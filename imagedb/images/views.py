from django.views.generic import ListView, DetailView

from imagedb.images.models import Image


class ImageListView(ListView):
    paginate_by = 10
    model = Image


class ImageDetailView(DetailView):
    model = Image


