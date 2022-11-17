from django.test import TestCase
from django.test import Client

import datetime
from flight_search.forms import SearchForm
from flight_search.models import *


class SearchFormTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.form_data = {
            'depature_city': 'Москва',
            'dest_city': 'Сочи',
            'max_transhipments': 1,
            'depart_date': str(datetime.date.today() + datetime.timedelta(days=7)),
            'return_date': None,
            'num_adults': 1,
            'num_children': 0,
            'luggage': True,
            'telegr_acc': '@my_account',
        }
        cities = [{
            'city_eng': 'Moscow',
            'city_rus': 'Москва',
            'code_eng': 'MSC',
            'code_rus': 'МСК',
        },
            {
                'city_eng': 'Sochi',
                'city_rus': 'Сочи',
                'code_eng': 'SCH',
                'code_rus': 'СОЧ',
            }
        ]
        for city in cities:
            CityCode.objects.create(**city)

    def test_search_form_is_valid_all_fields_filled(self):
        self.form_data['return_date'] = str(datetime.date.today() + datetime.timedelta(days=10))
        form = SearchForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_search_form_is_valid_no_return_flight(self):
        form = SearchForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_search_form_is_valid_no_luggage(self):
        self.form_data['luggage'] = False
        form = SearchForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_search_form_is_invalid_depart_date_in_past(self):
        self.form_data['depart_date'] = str(datetime.date.today() - datetime.timedelta(days=1))
        form = SearchForm(data=self.form_data)
        print(form.errors)
        self.assertFalse(form.is_valid())

    def test_search_form_is_invalid_return_date_before_depart_date(self):
        self.form_data['return_date'] = str(datetime.date.today() + datetime.timedelta(days=1))
        form = SearchForm(data=self.form_data)
        print(form.errors)
        self.assertFalse(form.is_valid())
