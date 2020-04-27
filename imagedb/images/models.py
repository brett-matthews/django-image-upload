from time import time
from django.db import models

from imagedb.images.infrastructure import PrivateMediaStorage


def user_directory_path(_, filename):
    return f'{round(time())}/{filename}'


class Image(models.Model):
    image = models.ImageField(upload_to=user_directory_path, storage=PrivateMediaStorage())


class ImageLabel(models.Model):
    image = models.ForeignKey(Image, related_name='labels', on_delete=models.CASCADE)
    label = models.CharField(max_length=255, db_index=True)
    confidence = models.FloatField()
