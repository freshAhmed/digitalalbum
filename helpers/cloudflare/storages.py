from storages.backends.s3 import S3Storage

class CloudflareStorage(S3Storage):
    pass


class StaticFileStorage(CloudflareStorage):
    location="static"


class MediaFileStorage(CloudflareStorage):
    location="media"
     