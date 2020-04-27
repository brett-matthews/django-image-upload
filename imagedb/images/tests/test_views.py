from django.test import Client, TestCase
from django.urls import reverse

from imagedb.images.models import Image, ImageLabel


class ImageDetailTest(TestCase):

    def setUp(self):
        self.image_name = 'fake_image'
        self.image = Image.objects.create(
            image=self.image_name
        )
        ImageLabel.objects.create(
            image=self.image,
            label='super_accurate_label',
            confidence=99.9,
        )
        ImageLabel.objects.create(
            image=self.image,
            label='no_way_label',
            confidence=1.0,
        )

        self.url = reverse('image-detail', args=(self.image.id,))

    def test_url_exists(self):
        self.assertEqual('/image/{}/'.format(self.image.id), self.url)

    def test_get_returns_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)