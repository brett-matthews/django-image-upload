from django.conf import settings
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from imagedb.images.models import Image, ImageLabel
from imagedb.images.services import AwsRekognitionLabels


class ImageListView(ListView):
    paginate_by = 10
    model = Image


class ImageDetailView(DetailView):
    model = Image


class ImageCreateView(CreateView):
    model = Image
    fields = ['image', ]
    success_url = reverse_lazy('image-list')

    def form_valid(self, form):

        self.object = form.save()
        labels = AwsRekognitionLabels().process_s3_object(
            s3_bucket=settings.AWS_STORAGE_BUCKET_NAME,
            s3_key=form.instance.image.name
        )

        for l in labels:
            ImageLabel.objects.create(
                image=form.instance,
                label=l['Name'],
                confidence=l['Confidence']
            )

        return HttpResponseRedirect(self.get_success_url())
