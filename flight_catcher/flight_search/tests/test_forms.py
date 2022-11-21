from django.test import TestCase
import datetime
from flight_search.forms import SearchForm
from flight_search.models import *


class SearchFormTest(TestCase):
    # setUpTestData: Run once to set up non-modified data for all class methods.
    @classmethod
    def setUpTestData(cls):
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

        test_search = {
            'depature_city': 'Москва',
            'dest_city': 'Сочи',
            'max_transhipments': 1,
            'depart_date': str(datetime.date.today() + datetime.timedelta(days=7)),
            'return_date': None,
            'num_adults': 1,
            'num_children': 0,
            'luggage': True,
            'telegr_acc': '@mytelegram_account',
        }

        Search.objects.create(**test_search)

    def setUp(self):
        # setUp: Run once for every test method to setup clean data.
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
        print('Test test_search_form_is_invalid_depart_date_in_past:', form.errors)
        self.assertFalse(form.is_valid())

    def test_search_form_is_invalid_return_date_before_depart_date(self):
        self.form_data['return_date'] = str(datetime.date.today() + datetime.timedelta(days=1))
        form = SearchForm(data=self.form_data)
        print('Test test_search_form_is_invalid_return_date_before_depart_date:', form.errors)
        self.assertFalse(form.is_valid())

    def test_search_form_is_invalid_no_depart_date(self):
        self.form_data['depart_date'] = None
        form = SearchForm(data=self.form_data)
        print('Test test_search_form_is_invalid_no_depart_date:', form.errors)
        self.assertFalse(form.is_valid())

    def test_search_form_is_invalid_no_adult_passenger(self):
        self.form_data['num_adults'] = 0
        form = SearchForm(data=self.form_data)
        print('Test test_search_form_is_invalid_no_adult_passenger:', form.errors)
        self.assertFalse(form.is_valid())

    def test_search_form_is_invalid_too_many_adult_passengers(self):
        self.form_data['num_adults'] = 11
        form = SearchForm(data=self.form_data)
        print('Test test_search_form_is_invalid_too_many_adult_passengers:', form.errors)
        self.assertFalse(form.is_valid())

    def test_search_form_is_invalid_too_many_children(self):
        self.form_data['num_children'] = 6
        form = SearchForm(data=self.form_data)
        print('Test test_search_form_is_invalid_too_many_children:', form.errors)
        self.assertFalse(form.is_valid())

    def test_search_form_is_invalid_too_many_transhipments(self):
        self.form_data['max_transhipments'] = 4
        form = SearchForm(data=self.form_data)
        print('Test test_search_form_is_invalid_too_many_transhipments:', form.errors)
        self.assertFalse(form.is_valid())

    def test_search_form_is_invalid_negative_amount_of_transhipments(self):
        self.form_data['max_transhipments'] = -1
        form = SearchForm(data=self.form_data)
        print('Test test_search_form_is_invalid_negative_amount_of_transhipments:', form.errors)
        self.assertFalse(form.is_valid())

    def test_search_form_is_invalid_telegr_acc_wrong_first_symb(self):
        self.form_data['telegr_acc'] = 'user123'
        form = SearchForm(data=self.form_data)
        print('Test test_search_form_is_invalid_telegr_acc_wrong_first_symb:', form.errors)
        self.assertFalse(form.is_valid())

    def test_search_form_is_invalid_telegr_acc_too_short(self):
        self.form_data['telegr_acc'] = '@user'
        form = SearchForm(data=self.form_data)
        print('Test test_search_form_is_invalid_telegr_acc_too_short:', form.errors)
        self.assertFalse(form.is_valid())

    def test_search_form_is_invalid_telegr_acc_contains_restricted_symb(self):
        self.form_data['telegr_acc'] = '@user!'
        form = SearchForm(data=self.form_data)
        print('Test test_search_form_is_invalid_telegr_acc_contains_restricted_symb:', form.errors)
        self.assertFalse(form.is_valid())

    def test_search_form_is_invalid_depart_city_doesnt_exist(self):
        self.form_data['depature_city'] = 'Миасс'
        form = SearchForm(data=self.form_data)
        print('Test test_search_form_is_invalid_depart_city_doesnt_exist:', form.errors)
        self.assertFalse(form.is_valid())

    def test_search_form_is_invalid_dest_city_doesnt_exist(self):
        self.form_data['dest_city'] = 'Миасс'
        form = SearchForm(data=self.form_data)
        print('Test test_search_form_is_invalid_dest_city_doesnt_exist:', form.errors)
        self.assertFalse(form.is_valid())

    def test_search_form_is_invalid_telegram_acc_already_made_request(self):
        self.form_data['telegr_acc'] = '@mytelegram_account'
        form = SearchForm(data=self.form_data)
        print('Test test_search_form_is_invalid_telegram_acc_already_made_request:', form.errors)
        self.assertFalse(form.is_valid())
