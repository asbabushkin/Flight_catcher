from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from .forms import SearchForm



# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('search_result')

    else:
        form = SearchForm()

    context = {
        'title': 'Автослежение за ценами на авиабилеты в Телеграм',
        'form': form,
    }
    return render(request, 'flight_search/index.html', context)


def search_res(request):
    return render(request, 'flight_search/result.html', {'title': 'Запрос принят!'})

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена<h1>')