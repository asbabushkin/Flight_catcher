from django.urls import path

from .views import *

urlpatterns = (
    path('', index, name='home'),
    path('result/', search_res, name='search_result'),
    path('project_description/', proj_descr, name='proj_descr'),
)

