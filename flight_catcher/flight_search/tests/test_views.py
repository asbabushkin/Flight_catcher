from django.test import TestCase
from django.urls import reverse

from flight_search.forms import *
from flight_search.models import *


class IndexPageTest(TestCase):
    def setUp(self):
        cities = [
            {
                "city_eng": "Moscow",
                "city_rus": "Москва",
                "code_eng": "MSC",
                "code_rus": "МСК",
            },
            {
                "city_eng": "Sochi",
                "city_rus": "Сочи",
                "code_eng": "SCH",
                "code_rus": "СОЧ",
            },
        ]
        for city in cities:
            CityCode.objects.create(**city)

        self.form_data = {
            "depart_city": "Москва",
            "dest_city": "Сочи",
            "max_transhipments": 1,
            "depart_date": str(datetime.date.today() + datetime.timedelta(days=7)),
            "return_date": str(datetime.date.today() + datetime.timedelta(days=14)),
            "num_adults": 1,
            "num_children": 0,
            "telegr_acc": "@my_account",
        }

    def test_redirects_to_success_page_on_success(self):
        resp = self.client.post(reverse("home"), self.form_data)
        self.assertRedirects(resp, reverse("search_result"))

    def test_views_search_form_is_invalid_depart_date_in_past(self):
        date_in_past = str(datetime.date.today() - datetime.timedelta(days=1))
        resp = self.client.post(reverse("home"), {"depart_date": date_in_past})
        self.assertEqual(resp.status_code, 200)
        self.assertFormError(resp, "form", "depart_date", "Дата вылета уже прошла.")

    def test_views_search_form_is_invalid_return_date_before_depart_date(self):
        resp = self.client.post(
            reverse("home"),
            {
                "depart_date": self.form_data["depart_date"],
                "return_date": str(datetime.date.today()),
            },
        )
        self.assertEqual(resp.status_code, 200)
        self.assertFormError(
            resp, "form", "return_date", "Дата возвращения ранее даты вылета."
        )

    def test_index_page_creates_correct_context(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)
        form_fields = {
            "depart_city": forms.fields.CharField,
            "dest_city": forms.fields.CharField,
            "max_transhipments": forms.fields.IntegerField,
            "depart_date": forms.fields.DateField,
            "return_date": forms.fields.DateField,
            "num_adults": forms.fields.IntegerField,
            "num_children": forms.fields.IntegerField,
            "telegr_acc": forms.fields.CharField,
        }

        for field_name, expected_value in form_fields.items():
            with self.subTest(field_name=field_name):
                form_field = resp.context.get("form").fields.get(field_name)
                self.assertIsInstance(form_field, expected_value)


class ResultPageTest(TestCase):
    def test_search_result_page_creates_correct_context(self):
        resp = self.client.get(reverse("search_result"))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context[-1]["title"], "Запрос принят!")


class ProjectDescriptionPageTest(TestCase):
    def test_proj_descr_page_creates_correct_context(self):
        resp = self.client.get(reverse("proj_descr"))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context[-1]["title"], "Как это работает")


class CommonPageTest(TestCase):
    def test_views_use_correct_templates(self):
        templates = {
            "home": "flight_search/index.html",
            "search_result": "flight_search/result.html",
            "proj_descr": "flight_search/project_description.html",
        }
        for key, expected_value in templates.items():
            with self.subTest(key=key):
                resp = self.client.get(reverse(key))
                self.assertEqual(resp.status_code, 200)
                self.assertTemplateUsed(resp, expected_value)

    def test_views_url_accessible_by_name(self):
        url_names = ["home", "search_result", "proj_descr"]
        for url_name in url_names:
            with self.subTest(url_name=url_names):
                resp = self.client.get(reverse(url_name))
                self.assertEqual(resp.status_code, 200)

    def test_views_url_exists_at_desired_location(self):
        urls = {
            "home": "",
            "search_result": "/result/",
            "proj_descr": "/project_description/",
        }
        for url_name, expected_value in urls.items():
            with self.subTest(url_name=url_name):
                resp = self.client.get(reverse(url_name))
                self.assertEqual(resp.status_code, 200)
