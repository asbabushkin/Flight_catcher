from django.urls import path

from .views import *

urlpatterns = (
    path('', index, name='home'),
    path('result/', SearchResultView.as_view(), name='search_result'),
    path('project_description/', ProjectDescriptionView.as_view(), name='proj_descr'),
)

