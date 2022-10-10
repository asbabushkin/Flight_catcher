from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('result/', search_res, name='search_result'),
]
