from django.db import models


class Traveller(models.Model):
    telegr_acc = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=20)
    email = models.CharField(max_length=30)


class SeatClass(models.Model):
    name = models.CharField(max_length=20, null=False)


class Search(models.Model):
    depature_city = models.CharField(max_length=50)
    dest_city = models.CharField(max_length=50)
    oneway_flight = models.BooleanField(default=False)
    max_transhipment = models.SmallIntegerField()
    return_date = models.DateField(null=False)
    arrival_date = models.DateField()
    num_adults = models.SmallIntegerField()
    num_infants = models.SmallIntegerField()
    num_childs = models.SmallIntegerField()
    luggage = models.BooleanField(default=False)
    seat_class = models.ForeignKey(SeatClass, on_delete=models.SET_NULL)
    search_init_date = models.DateTimeField(auto_now_add=True)
    search_until_date = models.DateTimeField(null=False)
    user_id = models.ForeignKey(Traveller, on_delete=models.SET_NULL)
