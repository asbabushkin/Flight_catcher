from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
def index(request):
    return HttpResponse('Flight cather start page')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена<h1>')