from uuid import uuid4

from django.db import models


def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = "news_archive/{filename}".format(
        filename='{}.{}'.format(uuid4().hex, ext))
    return file_path


class PartnersModel(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    img = models.ImageField(upload_to=upload_location, blank=True, null=True)

    def __str__(self):
        return str(self.title)

    @property
    def imageUrl(self):
        try:
            url = str(self.img.url)
        except:
            url = ''
        return url

