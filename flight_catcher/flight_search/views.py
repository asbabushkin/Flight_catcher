import os
from dotenv import load_dotenv
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from .forms import SearchForm
from telethon import TelegramClient, events, sync, connection as tel_connection



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
    # load_dotenv()
    # with TelegramClient('flight_catcher', int(os.getenv('TELEGRAM_API')), os.getenv('TELEGRAM_HASH')) as client:
    #     client.send_message(os.getenv('TELEGRAM_USER_NAME'),
    #                         message=f'Вы подписались на сервис мониторинга цен на авиабилеты "Flight catcher". Цены на интересующий перелет будут высылаться ежечасно в течении 3 суток.')
    return render(request, 'flight_search/result.html', {'title': 'Success!'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена<h1>')
