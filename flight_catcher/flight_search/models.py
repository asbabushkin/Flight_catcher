from django.db import models


class Traveller(models.Model):
    telegr_acc = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=20)
    email = models.CharField(max_length=30)

    def __str__(self):
        return self.telegr_acc


class SeatClass(models.Model):
    name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.name


class Search(models.Model):
    depature_city = models.CharField(max_length=50)
    dest_city = models.CharField(max_length=50)
    oneway_flight = models.BooleanField(default=False)
    max_transhipment = models.SmallIntegerField()
    arrival_date = models.DateField(null=False)
    return_date = models.DateField()
    num_adults = models.SmallIntegerField()
    num_infants = models.SmallIntegerField()
    num_childs = models.SmallIntegerField()
    luggage = models.BooleanField(default=False)
    seat_class = models.ForeignKey(SeatClass, null=True, on_delete=models.SET_NULL)
    search_init_date = models.DateTimeField(auto_now_add=True)
    search_until_date = models.DateTimeField(null=False)
    user_id = models.ForeignKey(Traveller, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.depature_city} - {self.dest_city}'

class SearchResult(models.Model):
    search_id = models.ForeignKey(Search, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    link = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'search {self.search_id}'