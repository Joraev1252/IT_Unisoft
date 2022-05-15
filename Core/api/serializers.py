from rest_framework import serializers
from Core.models.projects import ProjectsModel, ProjectCategoriesModel
from Core.models.about import AboutPageModel
from Core.models.partners import PartnersModel

from Core.blogs.mainpage import *


from Core.blogs.service import HeaderServices, MainService


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectsModel
        fields = '__all__'


class ProjectsCategoriesSerializer(serializers.ModelSerializer):
    projects = ProjectsSerializer(many=True)

    class Meta:
        model = ProjectCategoriesModel
        fields = ['id', 'title', 'projects']

class CategoryModeliesSerializer(serializers.ModelSerializer):
    projects = ProjectsSerializer(many=True)

    class Meta:
        model = ProjectCategoriesModel
        fields = '__all__'

#*************************************


class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = AboutPageModel
        fields = '__all__'


#***************************************


class PartnersSerializers(serializers.ModelSerializer):
    class Meta:
        model = PartnersModel
        fields = '__all__'




class BlogsServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeaderServices
        fields ='__all__'


class MainServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainService
        fields ='__all__'


class PartnersServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnersModel
        fields ='__all__'

#
# class MobileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MobileService
#         fields ='__all__'
#
#
# class SiteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SiteStructureService
#         fields ='__all__'
#




class MainPageHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPageHeaderModel
        fields ='__all__'


class MainPageAboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPageAboutModel
        fields ='__all__'


class MainPageServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPageServiceModel
        fields ='__all__'


class MainPageNumbersSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPageNumbersModel
        fields ='__all__'


class MainPageBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPageBlogModel
        fields ='__all__'
