from unittest.mock import patch

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase
from django.urls import reverse

from override_storage import override_storage

from imagedb.images.models import Image, ImageLabel


class ImageDetailViewTest(TestCase):

    def setUp(self):
        self.client = Client()
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


class ImageListViewTest(TestCase):

    def setUp(self):
        self.client = Client()

        self.image = Image.objects.create(
            image='image_1'
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

        self.image_2 = Image.objects.create(
            image='image_2'
        )
        ImageLabel.objects.create(
            image=self.image_2,
            label='super_accurate_label',
            confidence=99.9,
        )
        ImageLabel.objects.create(
            image=self.image_2,
            label='no_way_label',
            confidence=1.0,
        )

        self.url = reverse('image-list')

    def test_url_exists(self):
        self.assertEqual('/images/', self.url)

    def test_get_returns_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)


class ImageCreateViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('image-create')

        mock_aws_rekognition = patch('images.views.AwsRekognitionLabels.process_s3_object')
        self.mock_aws_rekognition = mock_aws_rekognition.start()
        self.addCleanup(mock_aws_rekognition.stop)

    def test_url_exists(self):
        self.assertEqual('/image/upload/', self.url)

    def test_post_returns_200(self):

        with override_storage():

            gif = (
                b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
                b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
                b'\x02\x4c\x01\x00\x3b'
            )

            upload_image = SimpleUploadedFile('test.gif', gif, content_type='image/gif')

            payload = {
                'image': upload_image
            }

            self.mock_aws_rekognition.return_value = [
                {
                    'Name': 'label_1',
                    'Confidence': '99.9'
                },
                {
                    'Name': 'label_2',
                    'Confidence': '9.9'
                }
            ]

            response = self.client.post(self.url, data=payload, format='multipart')

            self.assertEqual(response.status_code, 302)
