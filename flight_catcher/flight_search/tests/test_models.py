from django.test import TestCase
from flight_search.models import Search
import datetime

class SearchTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        Search.objects.create(depature_city='Москва',
                              dest_city='Екатеринбург',
                              oneway_flight=True,
                              max_transhipments=1,
                              depart_date='2022-11-28',
                              return_date='2022-11-30',
                              num_adults=1,
                              num_children=0,
                              luggage=False,
                              search_init_date=datetime.date.today(),
                              telegr_acc='@123',
                              phone_num='+79991234567',
                              email='123@ya.ru'
                              )

    # def setUp(self):
    #     print("setUp: Run once for every test method to setup clean data.")
    #     pass

    def test_depature_city_verbose_name(self):
        search = Search.objects.get(id=1)
        field_label = search._meta.get_field('depature_city').verbose_name
        self.assertEquals(field_label, 'depature city')

    def test_depature_city_max_length(self):
        search = Search.objects.get(id=1)
        max_length = search._meta.get_field('depature_city').max_length
        self.assertEquals(max_length, 50)

    def test_object_name_is_departure_city_hyphen_dest_city(self):
        search = Search.objects.get(id=1)
        expected_object_name = '%s - %s' % (search.depature_city, search.dest_city)
        self.assertEquals(expected_object_name, str(search))
