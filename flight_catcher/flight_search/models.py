from django.db import models
from django.http import HttpResponseRedirect
from django.urls import reverse


class AirportCode(models.Model):
    airport_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    iata_code = models.CharField(max_length=3)
    icao_code = models.CharField(max_length=4)
    rus_code = models.CharField(max_length=3)
    type = models.CharField(max_length=13)
    webpage = models.URLField()

    def __str__(self):
        return self.airport_name


class CityCode(models.Model):
    city_eng = models.CharField(max_length=50)
    city_rus = models.CharField(max_length=50)
    code_eng = models.CharField(max_length=3)
    code_rus = models.CharField(max_length=3)

    def __str__(self):
        return self.city_eng


class Search(models.Model):
    # depature_city = models.ForeignKey(CityCode, on_delete=models.SET_DEFAULT, related_name='depature_city', null=False, default='deleted')
    # dest_city = models.ForeignKey(CityCode, on_delete=models.SET_DEFAULT, related_name='dest_city', null=False, default='deleted')
    depart_city = models.CharField(max_length=50, verbose_name='Город вылета', help_text='Введите город вылета')
    dest_city = models.CharField(max_length=50, verbose_name='Город назначения', help_text='Введите город назначения')
    # oneway_flight = models.BooleanField(default=False, verbose_name='Рейс в один конец', help_text='Рейс в один конец')
    max_transhipments = models.SmallIntegerField(verbose_name='Количество пересадок',
                                                 help_text='Количество пересадок, не более 3')
    depart_date = models.DateField(verbose_name='Дата вылета', help_text='Введите дату вылета')
    return_date = models.DateField(null=True, verbose_name='Дата возвращения',
                                   help_text='Для перелетов в один конец оставьте пустым')
    num_adults = models.SmallIntegerField(verbose_name='Количество взрослых пассажиров', help_text='Не более 10')
    num_children = models.SmallIntegerField(null=True, verbose_name='Количество детей', help_text='Не более 5')
    num_infants = models.SmallIntegerField(null=True, verbose_name='Количество младенцев',
                                           help_text='Не более 1 на каждого взрослого')
    luggage = models.BooleanField(default=False, verbose_name='Багаж', help_text='Багаж')
    search_init_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления поиска',
                                            help_text='Дата добавления поиска')
    telegr_acc = models.CharField(max_length=50, verbose_name='Телеграм-аккаунт',
                                  help_text='Введите свой телеграм-аккаунт')
    phone_num = models.CharField(max_length=20, null=True, verbose_name='Телефон', help_text='Введите свой телефон')
    email = models.CharField(max_length=30, null=True, verbose_name='Эл. почта',
                             help_text='Введите свою электронную почту')

    def __str__(self):
        return f'{self.depart_city} - {self.dest_city}'

    # def get_absolute_url(self):
    #     return HttpResponseRedirect(reverse('search_result'))


class SearchResult(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    link = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)
    search = models.ForeignKey('Search', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'search {self.search}'
