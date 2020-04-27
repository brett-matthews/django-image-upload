from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from imagedb.images.models import Image


class ImageListView(ListView):
    paginate_by = 10
    model = Image


class ImageDetailView(DetailView):
    model = Image


class ImageCreateView(CreateView):
    model = Image
    form_class = None

