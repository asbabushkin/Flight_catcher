import datetime
import string

from django import forms
from django.core.exceptions import ValidationError
from django.forms import DateInput, NumberInput, TextInput

from .models import CityCode, Search


class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = [
            "depart_city",
            "dest_city",
            "max_transhipments",
            "depart_date",
            # "return_date",
            "num_adults",
            "num_children",
            "luggage",
            "telegr_acc",
        ]

        widgets = {
            "depart_city": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "",
                }
            ),
            "dest_city": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "",
                }
            ),
            "max_transhipments": NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "",
                }
            ),
            "depart_date": DateInput(
                format="%d-%m-%Y",
                attrs={
                    "class": "form-control",
                    "type": "date",
                },
            ),
            # 'return_date': DateInput(attrs={
            #     'class': 'form-control',
            #     'type': 'date',
            # }),
            "num_adults": NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "1",
                }
            ),
            "num_children": NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "0",
                }
            ),
            "telegr_acc": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["depart_city"].label = "Откуда"
        self.fields["dest_city"].label = "Куда"
        self.fields["max_transhipments"].label = "Пересадок не более"
        self.fields["depart_date"].label = "Дата вылета"
        # self.fields['return_date'].label = 'Дата возвращения'
        # self.fields["return_date"].required = False
        self.fields["num_adults"].label = "Взрослых"
        self.fields["num_children"].label = "Детей"
        self.fields["num_children"].required = False
        self.fields["luggage"].label = "Багаж"
        self.fields["telegr_acc"].label = "Телеграм аккаунт"

    def clean_depart_city(self):
        depart_city = self.cleaned_data["depart_city"]
        if not CityCode.objects.filter(city_rus=depart_city):
            raise ValidationError("Город вылета не найден!")
        return depart_city

    def clean_dest_city(self):
        dest_city = self.cleaned_data["dest_city"]
        if not CityCode.objects.filter(city_rus=dest_city):
            raise ValidationError("Город назначения не найден!")
        return dest_city

    def clean_depart_date(self):
        if self.cleaned_data["depart_date"] < datetime.date.today():
            raise ValidationError("Дата вылета уже прошла.")
        return self.cleaned_data["depart_date"]

    # def clean_return_date(self):
    #     if self.cleaned_data['return_date'] is not None:
    #         if self.cleaned_data['return_date'] < datetime.date.today():
    #             raise ValidationError('Дата возвращения уже прошла.')
    #         elif self.cleaned_data['return_date'] < self.cleaned_data['depart_date']:
    #             raise ValidationError('Дата возвращения ранее даты вылета.')
    #     return self.cleaned_data['return_date']

    def clean_max_transhipments(self):
        if (
            self.cleaned_data["max_transhipments"] < 0
            or self.cleaned_data["max_transhipments"] > 1
        ):
            raise ValidationError("Не более 1 пересадки")
        return self.cleaned_data["max_transhipments"]

    def clean_num_adults(self):
        if self.cleaned_data["num_adults"] < 1 or self.cleaned_data["num_adults"] > 10:
            raise ValidationError("Не менее 1 и не более 10 взрослых пассажиров.")
        return self.cleaned_data["num_adults"]

    def clean_num_children(self):
        if self.cleaned_data["num_children"] is not None:
            if (
                self.cleaned_data["num_children"] < 0
                or self.cleaned_data["num_children"] > 5
            ):
                raise ValidationError("Не более 5 детей")
            return self.cleaned_data["num_children"]

    def clean_telegr_acc(self):
        acc_symb = list(string.digits + string.ascii_lowercase + "_")
        if self.cleaned_data["telegr_acc"][0] != "@":
            raise ValidationError('Телеграм-аккаунт должен начинаться со знака "@"')
        elif len(self.cleaned_data["telegr_acc"]) < 6:
            raise ValidationError("Телеграм-аккаунт имеет длину не менее 6 символов")
        elif (
            len(Search.objects.filter(telegr_acc=self.cleaned_data["telegr_acc"])) > 3
        ):
            raise ValidationError(
                "Один пользователь может создавать не более 3 поисков!"
            )
        for i in self.cleaned_data["telegr_acc"][1:]:
            if i not in acc_symb:
                raise ValidationError("Телеграм-аккаунт содержит недопустимые символы")

        return self.cleaned_data["telegr_acc"]
