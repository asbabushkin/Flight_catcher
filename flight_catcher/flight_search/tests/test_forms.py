from django.test import TestCase

import datetime
from django.utils import timezone
from flight_search.forms import SearchForm


class SearchFormTest(TestCase):
    def setUp(self):
        self.form_data = {
            'depature_city': 'Москва',
            'dest_city': 'Екатеринбург',
            'max_transhipments': 1,
            'depart_date': str(datetime.date.today() + datetime.timedelta(days=7)),
            'return_date': None,
            'num_adults': 1,
            'num_children': 0,
            'luggage': False,
            'telegr_acc': '@my_account',
        }

    def test_search_form_depart_date_in_past(self):
        self.form_data['depart_date'] = str(datetime.date.today() - datetime.timedelta(days=1))
        form = SearchForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_search_form_return_date_before_depart_date(self):
        self.form_data['return_date'] = str(datetime.date.today() + datetime.timedelta(days=1))
        form = SearchForm(data=self.form_data)
        self.assertFalse(form.is_valid())

