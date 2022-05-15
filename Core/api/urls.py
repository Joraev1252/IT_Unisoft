from django.urls import path, include

from Core.api.views import blog_list_about, project_detail, category_detail
from Core.views import *
from Core.api.views import partners
from rest_framework import routers
from Core.api.views import *

app_name = 'Core'

urlpatterns = [
    path('blogs/about/', blog_list_about),
    path('blogs/projects/', ProjectsListView.as_view()),
    path('blogs/categories/', ProjectsCategoriesView.as_view()),
    path('blogs/projects/<int:pk>', project_detail),
    path('blogs/categories/<int:pk>', category_detail),
    path('blogs/partners/', partners),



    path('service/header/', blog_list),
    path('service/header/<int:pk>/', blog_detail),
    path('service/main/', ItMainList.as_view()),


    #nur
    path('mainpage/header/', MainPageHeaderView.as_view()),
    path('mainpage/header/<int:pk>/', MainPageHeaderIdView.as_view()),
    path('mainpage/about/', MainPageAboutView.as_view()),
    path('mainpage/about/<int:pk>/', MainPageAboutIdView.as_view()),
    path('mainpage/service/', MainPageServiceView.as_view()),
    path('mainpage/service/<int:pk>/', MainPageServiceIdView.as_view()),
    path('mainpage/numbers/', MainPageNumbersView.as_view()),
    path('mainpage/numbers/<int:pk>/', MainPageNumbersIdView.as_view()),
    path('mainpage/blog/', MainPageBlogView.as_view()),
    path('mainpage/blog/<int:pk>/', MainPageBlogIdView.as_view()),


]
