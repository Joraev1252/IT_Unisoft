from uuid import uuid4

from django.db import models


def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = "news_archive/{filename}".format(
        filename='{}.{}'.format(uuid4().hex, ext))
    return file_path


class ProjectCategoriesModel(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return str(self.title)



class ProjectsModel(models.Model):
    category = models.ForeignKey(ProjectCategoriesModel, related_name='projects', on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to=upload_location, blank=True, null=True)
    body_title = models.CharField(max_length=255)
    text = models.TextField()
    img2 = models.ImageField(upload_to=upload_location, blank=True, null=True)

    @property
    def imageUrl(self):
        try:
            url = str(self.img.url)
        except:
            url = ''
        return url

    @property
    def image2Url(self):
        try:
            url = str(self.img2.url)
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.title)

