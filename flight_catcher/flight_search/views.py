from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound

from .forms import SearchForm


# Create your views here.
def index(request):
    error = ''
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('search_result')
        else:
            error = 'Smth wrong with form...'

    form = SearchForm()
    context = {
        'title': 'Flight catcher',
        'form': form,
        'error': error,
    }

    return render(request, 'flight_search/index.html', context)


def search_res(request):
    return render(request, 'flight_search/result.html', {'title': 'Результат'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена<h1>')
