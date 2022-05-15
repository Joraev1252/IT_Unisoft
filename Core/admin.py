from django.contrib import admin
from Core.models.projects import ProjectsModel, ProjectCategoriesModel

from Core.models.about import AboutPageModel
from Core.models.partners import PartnersModel

from Core.blogs.service import HeaderServices, MainService
from Core.blogs.mainpage import *

admin.site.register(HeaderServices)
admin.site.register(MainService)



#nur
admin.site.register(MainPageHeaderModel)
admin.site.register(MainPageAboutModel)
admin.site.register(MainPageServiceModel)
admin.site.register(MainPageNumbersModel)
admin.site.register(MainPageBlogModel)





admin.site.register(ProjectsModel)
admin.site.register(ProjectCategoriesModel)


admin.site.register(AboutPageModel)

admin.site.register(PartnersModel)