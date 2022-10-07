from django.db import models


class AirportCode(models.Model):
    airport_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    iata_code = models.CharField(max_length=3)
    icao_code = models.CharField(max_length=4)
    Rus_code = models.CharField(max_length=3)
    type = models.CharField(max_length=8)
    webpage = models.URLField(max_length=50)

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
    depature_city = models.ForeignKey(CityCode, on_delete=models.SET_DEFAULT, related_name='depature_city', null=False, default='deleted')
    dest_city = models.ForeignKey(CityCode, on_delete=models.SET_DEFAULT, related_name='dest_city', null=False, default='deleted')
    oneway_flight = models.BooleanField(default=False)
    max_transhipments = models.SmallIntegerField(default=0)
    depart_date = models.DateField()
    return_date = models.DateField(null=True)
    num_adults = models.SmallIntegerField()
    num_children = models.SmallIntegerField(null=True)
    luggage = models.BooleanField(default=False)
    search_init_date = models.DateTimeField(auto_now_add=True)
    telegr_acc = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f'{self.depature_city} - {self.dest_city}'


class SearchResult(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    link = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)
    search = models.ForeignKey('Search', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'search {self.search}'
