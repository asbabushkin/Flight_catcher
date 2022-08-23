from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from .models import *


# Create your views here.
def index(request):
    seatclass = SeatClass.objects.all()
    return render(request, 'flight_search/index.html', {'title': 'Flight catcher', 'seatclass': seatclass})

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена<h1>')