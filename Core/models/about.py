from django.db import models
from django.urls import reverse
from uuid import uuid4
from django.db.models.signals import pre_save



def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = "news_archive/{filename}".format(
        filename='{}.{}'.format(uuid4().hex, ext))
    return file_path


class AboutPageModel(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    body = models.TextField(max_length=355, null=True, blank=True)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    video = models.FileField(blank=True, null=True)
    body_2 = models.TextField(max_length=355, null=True, blank=True)



    @property
    def imageURL(self):
        try:
            url = str(self.image.url)
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.title)



    # def get_absolute_url(self):
    #     return reverse("News:NewsViews", args=[str(self.id)])


# from django.db import models
#
# class BlogModel(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     title = models.CharField(max_length=100, blank=True, default='')
#     body = models.TextField()
#
#     class Meta:
#         ordering =['created']
#
#     def __str__(self):
#         return str(self.title)