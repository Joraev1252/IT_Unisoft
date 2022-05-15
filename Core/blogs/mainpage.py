from uuid import uuid4
from django.db import models


def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'service_archive/{filename}'.format(
        filename='{}.{}'.format(uuid4().hex, ext)
    )
    return file_path


class MainPageHeaderModel(models.Model):
    title1 = models.CharField(max_length=50)
    image1 = models.ImageField(upload_to=upload_location, null=True,  blank=True)

    title2 = models.CharField(max_length=50)
    image2 = models.ImageField(upload_to=upload_location, null=True,  blank=True)

    title3 = models.CharField(max_length=50)
    image3 = models.ImageField(upload_to=upload_location, null=True,  blank=True)


    @property
    def imageURL(self):
        try:
            url = str(self.image.url)
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.title1)

class MainPageAboutModel(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()

    def __str__(self):
        return str(self.title)


class MainPageServiceModel(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    image1 = models.ImageField(upload_to=upload_location, null=True,  blank=True)
    image1_title = models.CharField(max_length=50)
    image2 = models.ImageField(upload_to=upload_location, null=True,  blank=True)
    image2_title = models.CharField(max_length=50)
    image3 = models.ImageField(upload_to=upload_location, null=True,  blank=True)
    image3_title = models.CharField(max_length=50)
    image4 = models.ImageField(upload_to=upload_location, null=True,  blank=True)
    image4_title = models.CharField(max_length=50)

    def __str__(self):
        return str(self.title)

    @property
    def imageURL(self):
        try:
            url = str(self.image.url)
        except:
            url = ''
        return url

class MainPageNumbersModel(models.Model):
    title = models.CharField(max_length=50)
    num1 = models.IntegerField()
    title1 = models.CharField(max_length=50)
    num2 = models.IntegerField()
    title2 = models.CharField(max_length=50)
    num3 = models.IntegerField()
    title3 = models.CharField(max_length=50)


    def __str__(self):
        return str(self.title)


class MainPageBlogModel(models.Model):
    title = models.CharField(max_length=50)
    image1 = models.ImageField(upload_to=upload_location, null=True,  blank=True)
    image1_title = models.CharField(max_length=50)
    image2 = models.ImageField(upload_to=upload_location, null=True,  blank=True)
    image2_title = models.CharField(max_length=50)
    image3 = models.ImageField(upload_to=upload_location, null=True,  blank=True)
    image3_title = models.CharField(max_length=50)
    image4 = models.ImageField(upload_to=upload_location, null=True,  blank=True)
    image4_title = models.CharField(max_length=50)
    
    @property
    def imageURL(self):
        try:
            url = str(self.image.url)
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.title)









    
    
