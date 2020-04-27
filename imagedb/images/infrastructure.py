from django.conf import  settings
from storages.backends.s3boto3 import S3Boto3Storage


class PrivateMediaStorage(S3Boto3Storage):
    default_acl = 'private'
    file_overwrite = False
    custom_domain = False
    region_name = settings.AWS_DEFAULT_REGION

