from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from .models import *
from .forms import *


# Create your views here.
def index(request):
    seatclass = SeatClass.objects.all()
    form = AddSearchForm()
    context = {
        'title': 'Flight catcher',
        'form': form,
        'seatclass': seatclass,
    }
    return render(request, 'flight_search/index.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена<h1>')