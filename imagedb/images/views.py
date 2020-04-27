from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from imagedb.images.models import Image, ImageLabel
from imagedb.images.services import AwsRekognitionLabels, AwsS3PresignedUrl


class ImageListView(ListView):
    paginate_by = 10
    model = Image
    ordering = ['-pk']


class ImageDetailView(DetailView):
    model = Image


class ImageCreateView(CreateView):
    model = Image
    fields = ['image', ]
    success_url = reverse_lazy('image-list')

    def form_valid(self, form):

        self.object = form.save()
        labels = AwsRekognitionLabels.get_labels(
            image=self.object
        )

        for l in labels:
            ImageLabel.objects.create(
                image=form.instance,
                label=l['Name'],
                confidence=l['Confidence']
            )

        return HttpResponseRedirect(self.get_success_url())

    # TODO dependency injection here?

class ImageDownloadView(View):

    template_name = 'images/image_download.html'

    def get(self, request, pk):

        try:
            image = Image.objects.get(id=pk)
        except Image.DoesNotExist:
            return HttpResponseNotFound()

        url = AwsS3PresignedUrl.get_image_url(
            image=image
        )

        return render(
            request, self.template_name, {'url': url}
        )
