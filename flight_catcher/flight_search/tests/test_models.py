import datetime

from django.test import TestCase

from flight_search.models import Search


class SearchModelTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_search = Search.objects.create(
            depart_city="Москва",
            dest_city="Екатеринбург",
            max_transhipments=1,
            depart_date="2022-11-28",
            return_date="2022-11-30",
            num_adults=1,
            num_children=0,
            luggage=False,
            search_init_date=datetime.date.today(),
            telegr_acc="@123",
            phone_num="+79991234567",
            email="123@ya.ru",
        )

    # def setUp(self):
    #     print("setUp: Run once for every test method to setup clean data.")
    #     pass

    def test_depart_city_max_length(self):
        test_search = SearchModelTestClass.test_search
        # search = Search.objects.get(id=1)
        max_length = test_search._meta.get_field("depart_city").max_length
        self.assertEquals(max_length, 50)

    def test_object_name_is_depart_city_hyphen_dest_city(self):
        test_search = SearchModelTestClass.test_search
        # search = Search.objects.get(id=1)
        expected_object_name = "%s - %s" % (
            test_search.depart_city,
            test_search.dest_city,
        )
        self.assertEquals(expected_object_name, str(test_search))

    def test_search_model_verbose_names(self):
        verboses = {
            "depart_city": "Город вылета",
            "dest_city": "Город назначения",
            "max_transhipments": "Количество пересадок",
            "depart_date": "Дата вылета",
            "return_date": "Дата возвращения",
            "num_adults": "Количество взрослых пассажиров",
            "num_children": "Количество детей",
            "num_infants": "Количество младенцев",
            "luggage": "Багаж",
            "search_init_date": "Дата добавления поиска",
            "telegr_acc": "Телеграм-аккаунт",
            "phone_num": "Телефон",
            "email": "Эл. почта",
        }
        test_search = SearchModelTestClass.test_search
        # test_search = Search.objects.get(id=1)
        for key, expected_value in verboses.items():
            with self.subTest(key=key):
                self.assertEqual(
                    test_search._meta.get_field(key).verbose_name, expected_value
                )

    def test_search_model_help_texts(self):
        help_texts = {
            "depart_city": "Введите город вылета",
            "dest_city": "Введите город назначения",
            "max_transhipments": "Количество пересадок, не более 3",
            "depart_date": "Введите дату вылета",
            "return_date": "Для перелетов в один конец оставьте пустым",
            "num_adults": "Не более 10",
            "num_children": "Не более 5",
            "num_infants": "Не более 1 на каждого взрослого",
            "luggage": "Багаж",
            "search_init_date": "Дата добавления поиска",
            "telegr_acc": "Введите свой телеграм-аккаунт",
            "phone_num": "Введите свой телефон",
            "email": "Введите свою электронную почту",
        }
        test_search = SearchModelTestClass.test_search
        # search = Search.objects.get(id=1)
        for key, expected_value in help_texts.items():
            with self.subTest(key=key):
                self.assertEqual(
                    test_search._meta.get_field(key).help_text, expected_value
                )
