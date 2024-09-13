from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class PublicMediaStorage(S3Boto3Storage):
    def __init__(self, *args, **kwargs):
        kwargs['file_overwrite'] = False
        super().__init__(*args, **kwargs)