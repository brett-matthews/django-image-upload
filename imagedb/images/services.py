import boto3


class AwsS3RekognitionLabels(object):

    @staticmethod
    def process_s3_object(s3_bucket, s3_key):

        client = boto3.client('rekognition')

        response = client.detect_labels(
            Image={
                'S3Object': {
                    'Bucket': s3_bucket,
                    'Name': s3_key
                }
            }
        )

        return response['Labels']
