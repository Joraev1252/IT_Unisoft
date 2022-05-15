from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Core.api.serializers import BlogSerializers, ProjectsSerializer, ProjectsCategoriesSerializer, CategoryModeliesSerializer
from Core.models.about import AboutPageModel
from Core.models.projects import ProjectsModel, ProjectCategoriesModel
from Core.models.partners import PartnersModel
from Core.api.serializers import PartnersSerializers
from django.http import HttpResponse, JsonResponse
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from Core.api.serializers import BlogsServiceSerializer, MainServiceSerializer, PartnersServiceSerializer
from Core.blogs.service import HeaderServices, MainService

from Core.api.serializers import *


@api_view(['GET', 'POST'])
def blog_list_about(request):

    if request.method == 'GET':
        blogs = AboutPageModel.objects.all()
        serializer = BlogSerializers(blogs, many=True)
        return Response(serializer.data)

    if request.method != 'GET':
        return Response({'response': 'We get only GET method!'})


@api_view(['GET', 'PUT', 'DELETE'])
def project_detail(request, pk):
    try:
        blog = ProjectsModel.objects.get(pk=pk)
    except ProjectsModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProjectsSerializer(blog)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):
    try:
        blog = ProjectCategoriesModel.objects.get(pk=pk)
    except ProjectsModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProjectsCategoriesSerializer(blog)
        return Response(serializer.data)


    # elif request.method == 'PUT':
    #     serializer = SnippetSerializer(snippet, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # elif request.method == 'DELETE':
    #     snippet.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def partners(request):

    if request.method == 'GET':
        blogs = PartnersModel.objects.all()
        serializer = PartnersSerializers(blogs, many=True)
        return Response(serializer.data)




@api_view(['GET', 'POST'])
def blog_list(request):

    if request.method == 'GET':
        blogs = HeaderServices.objects.all()
        serializer = BlogsServiceSerializer(blogs, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def blog_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = HeaderServices.objects.get(pk=pk)
    except HeaderServices.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BlogsServiceSerializer(snippet)
        return Response(serializer.data)\



class AboutAPI(APIView):
    def get(self, request):
        it = MainService.object_all()
        serializer = MainServiceSerializer(it, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = MainServiceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            error = {'msg': 'Data has been created Successfully'}
            return Response(error)
        return Response({'msg': serializer.errors})


class ItMainList(GenericAPIView, ListModelMixin):
    queryset = MainService.objects.all()
    serializer_class = MainServiceSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

#nur

class MainPageHeaderIdView(GenericAPIView, RetrieveModelMixin):
        queryset = MainPageHeaderModel.objects.all()
        serializer_class = MainPageHeaderSerializer

        def get(self, request, *args, **kwargs):
            return self.retrieve(request, *args, **kwargs)

class MainPageAboutIdView(GenericAPIView, RetrieveModelMixin):
        queryset = MainPageAboutModel.objects.all()
        serializer_class = MainPageAboutSerializer

        def get(self, request, *args, **kwargs):
            return self.retrieve(request, *args, **kwargs)

class MainPageServiceIdView(GenericAPIView, RetrieveModelMixin):
        queryset = MainPageServiceModel.objects.all()
        serializer_class = MainPageServiceSerializer

        def get(self, request, *args, **kwargs):
            return self.retrieve(request, *args, **kwargs)

class MainPageNumbersIdView(GenericAPIView, RetrieveModelMixin):
        queryset = MainPageNumbersModel.objects.all()
        serializer_class = MainPageNumbersSerializer

        def get(self, request, *args, **kwargs):
            return self.retrieve(request, *args, **kwargs)

class MainPageBlogIdView(GenericAPIView, RetrieveModelMixin):
        queryset = MainPageBlogModel.objects.all()
        serializer_class = MainPageBlogSerializer

        def get(self, request, *args, **kwargs):
            return self.retrieve(request, *args, **kwargs)





class MainPageHeaderView(GenericAPIView, ListModelMixin):
        queryset = MainPageHeaderModel.objects.all()
        serializer_class = MainPageHeaderSerializer

        def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)

class MainPageAboutView(GenericAPIView, ListModelMixin):
        queryset = MainPageAboutModel.objects.all()
        serializer_class = MainPageAboutSerializer

        def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)

class MainPageServiceView(GenericAPIView, ListModelMixin):
        queryset = MainPageServiceModel.objects.all()
        serializer_class = MainPageServiceSerializer

        def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)

class MainPageNumbersView(GenericAPIView, ListModelMixin):
        queryset = MainPageNumbersModel.objects.all()
        serializer_class = MainPageNumbersSerializer

        def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)

class MainPageBlogView(GenericAPIView, ListModelMixin):
        queryset = MainPageBlogModel.objects.all()
        serializer_class = MainPageBlogSerializer

        def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)
