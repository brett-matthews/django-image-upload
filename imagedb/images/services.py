import boto3

from django.conf import settings

from imagedb.images.models import Image


class AwsRekognitionLabels(object):

    @staticmethod
    def get_labels(image: Image):

        client = boto3.client('rekognition')

        response = client.detect_labels(
            Image={
                'S3Object': {
                    'Bucket': settings.AWS_STORAGE_BUCKET_NAME,
                    'Name': image.image.name
                }
            }
        )

        return response['Labels']


class AwsS3PresignedUrl(object):

    @staticmethod
    def get_image_url(image: Image):

        s3_client = boto3.client('s3')

        response = s3_client.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': settings.AWS_STORAGE_BUCKET_NAME,
                'Key': image.image.name
            },
            ExpiresIn=300
        )

        return response
