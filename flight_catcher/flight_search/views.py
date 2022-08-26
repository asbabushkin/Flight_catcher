from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound

from .models import *
from .forms import *


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = NewSearchForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('search_result')

    else:
        form = NewSearchForm()

    return render(request, 'flight_search/index.html', {'title': 'Flight catcher', 'form': form})

def search_res(request):
    return render(request, 'flight_search/result.html', {'title': 'Результат'})

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена<h1>')
