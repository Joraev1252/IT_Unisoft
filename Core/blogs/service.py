from uuid import uuid4

from django.db import models


def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'service_archive/{filename}'.format(
        filename='{}.{}'.format(uuid4().hex, ext)
    )
    return file_path


class HeaderServices(models.Model):
    title = models.CharField('title', max_length=50)
    body_one = models.TextField('body_1')
    body_two = models.TextField('body_2')
    body_three = models.TextField('body_3')
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)

    def __str__(self):
        return str(self.title)


    @property
    def imageURL(self):
        try:
            url = str(self.image.url)
        except:
            url = ''
        return url


class MainService(models.Model):
    main_title = models.CharField('services', max_length=20, null=True, blank=True)

    blog_title = models.CharField('blog_title', max_length=30)
    comment = models.TextField('comment',)

    list_body = models.TextField('body',)
    page_body = models.TextField('body',)
    photo_body = models.TextField('body',)
    pages_body = models.TextField('body',)
    ios_body = models.TextField('body',)
    image_all = models.ImageField(upload_location, 'image', null=True, blank=True)

    def __str__(self):
        return str(self.blog_title)

    @property
    def imageURL(self):
        try:
            url = str(self.image.url)
        except:
            url = ''
        return url
#
#
# class MobileService(models.Model):
#     phone_title = models.CharField('blog_title', max_length=30)
#     comment = models.TextField('comment',)
#
#     Android = models.TextField('body',)
#     Automa= models.TextField('body',)
#     Ios = models.TextField('body',)
#     Google = models.TextField('body',)
#     Appstore = models.TextField('body',)
#     image_phone = models.ImageField(upload_location, 'image', null=True, blank=True)
#
#     def __str__(self):
#         return str(self.phone_title)
#
#     @property
#     def imageURL(self):
#         try:
#             url = str(self.image.url)
#         except:
#             url = ''
#         return url
#
#
# class SiteStructureService(models.Model):
#     Site_title = models.CharField('blog_title', max_length=30)
#     comment = models.TextField('comment',)
#
#     Online = models.TextField('body',)
#     Landing = models.TextField('body',)
#     Technical = models.TextField('body',)
#     Corporate = models.TextField('body',)
#     Complex = models.TextField('body',)
#     image_site = models.ImageField(upload_location, 'image', null=True, blank=True)
#
#     def __str__(self):
#         return str(self.Site_title)
#
#     @property
#     def imageURL(self):
#         try:
#             url = str(self.image.url)
#         except:
#             url = ''
#         return url
