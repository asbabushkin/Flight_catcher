from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import FormView, View, CreateView

from .forms import SearchForm


def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('search_result')
            return HttpResponseRedirect(reverse('search_result'))

    else:
        form = SearchForm()

    context = {
        'title': 'Мониторинг цен на авиабилеты',
        'form': form,
    }
    return render(request, 'flight_search/index.html', context)


class SearchResultView(View):
    def get(self, request):
        return render(request, 'flight_search/result.html', {'title': 'Запрос принят!'})


class ProjectDescriptionView(View):
    def get(self, request):
        return render(request, 'flight_search/project_description.html', {'title': 'Как это работает?'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена<h1>')
