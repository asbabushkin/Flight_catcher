from django.test import TestCase
from django.urls import reverse
from flight_search.forms import *
from flight_search.models import *


class IndexPageTest(TestCase):
    def setUp(self):
        self.form_data = {
            'depature_city': 'Москва',
            'dest_city': 'Екатеринбург',
            'max_transhipments': 1,
            'depart_date': str(datetime.date.today() + datetime.timedelta(days=7)),
            #'return_date': None,
            'num_adults': 1,
            'num_children': 0,
            #'luggage': False,
            'telegr_acc': '@my_account',
        }




    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        # print(resp.context)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'flight_search/index.html')

    def test_redirects_to_success_page_on_success(self):
        # form_data = {
        #     'depature_city': 'Москва',
        #     'dest_city': 'Екатеринбург',
        #     'max_transhipments': 1,
        #     'depart_date': str(datetime.date.today() + datetime.timedelta(days=7)),
        #     # 'return_date': None,
        #     'num_adults': 1,
        #     'num_children': 0,
        #     # 'luggage': False,
        #     'telegr_acc': '@my_account',
        # }
        # form = SearchForm(data=form_data)
        resp = self.client.post(reverse('home'), self.form_data)
        print(resp.status_code)

        #print(form.errors)
        self.assertRedirects(resp, reverse('search_result'))


    def test_form_invalid_depart_date_in_past(self):
        date_in_past = str(datetime.date.today() - datetime.timedelta(days=1))
        #self.form_data['depart_date'] = date_in_past
        resp = self.client.post(reverse('home'), {'depart_date': date_in_past})
        self.assertEqual(resp.status_code, 200)
        self.assertFormError(resp, 'form', 'depart_date', 'Дата вылета уже прошла.')