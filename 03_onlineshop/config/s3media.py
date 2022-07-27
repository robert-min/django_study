from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    location = ""
    bucket_name = "robert-online-media"
    region_name = "ap-northeast-2"
    custom_domain = f"s3.{region_name}.amazon.com/{bucket_name}"
    file_overwrite = False
