from rest_framework.generics import ListAPIView

from Core.models.projects import ProjectsModel, ProjectCategoriesModel
from Core.api.serializers import ProjectsSerializer, ProjectsCategoriesSerializer


class ProjectsListView(ListAPIView):
    queryset = ProjectsModel.objects.all()
    serializer_class = ProjectsSerializer


class ProjectsCategoriesView(ListAPIView):
    queryset = ProjectCategoriesModel.objects.all()
    serializer_class = ProjectsCategoriesSerializer



