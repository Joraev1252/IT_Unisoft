from uuid import uuid4

from django.db import models


from django.db import models

# Create your models here.


def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'partners_archive/{filename}'.format(
        filename='{}.{}'.format(uuid4().hex, ext)
    )
    return file_path


class PartnersModels(models.Model):
    title = models.CharField('title', max_length=100)
    logo_1 = models.ImageField(upload_to=upload_location, null=True,  blank=True)
    logo_2 = models.ImageField(upload_to=upload_location, null=True,  blank=True)
    logo_3 = models.ImageField(upload_to=upload_location, null=True,  blank=True)
    logo_4 = models.ImageField(upload_to=upload_location, null=True,  blank=True)
    logo_5 = models.ImageField(upload_to=upload_location, null=True,  blank=True)
    logo_6 = models.ImageField(upload_to=upload_location, null=True,  blank=True)
    logo_7 = models.ImageField(upload_to=upload_location, null=True,  blank=True)
    logo_8 = models.ImageField(upload_to=upload_location, null=True,  blank=True)
    logo_9 = models.ImageField(upload_to=upload_location, null=True,  blank=True)
    logo_10 = models.ImageField(upload_to=upload_location, null=True,  blank=True)
    logo_11 = models.ImageField(upload_to=upload_location, null=True,  blank=True)
    logo_12 = models.ImageField(upload_to=upload_location, null=True,  blank=True)
    logo_13 = models.ImageField(upload_to=upload_location, null=True,  blank=True)
    logo_14 = models.ImageField(upload_to=upload_location, null=True,  blank=True)
    logo_15 = models.ImageField(upload_to=upload_location, null=True,  blank=True)
    logo_16 = models.ImageField(upload_to=upload_location, null=True,  blank=True)
    logo_17 = models.ImageField(upload_to=upload_location, null=True,  blank=True)
    logo_18 = models.ImageField(upload_to=upload_location, null=True,  blank=True)
    logo_19 = models.ImageField(upload_to=upload_location, null=True,  blank=True)
    logo_20 = models.ImageField(upload_to=upload_location, null=True,  blank=True)



    def __str__(self):
        return str(self.title)



    @property
    def imageURL(self):
        try:
            url = str(self.image.url)
        except:
            url = ''
        return url

