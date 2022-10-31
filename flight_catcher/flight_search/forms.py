from django import forms
from django.core.exceptions import ValidationError
from django.forms import TextInput, DateTimeInput, NumberInput, DateInput, DateField
import datetime
from flight_catcher import settings
from .models import Search, CityCode


# from .widgets import DatePickerInput


class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ['depature_city', 'dest_city', 'max_transhipments', 'depart_date', 'return_date',
                  'num_adults', 'num_children', 'luggage', 'telegr_acc', ]

        widgets = {
            'depature_city': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '',
            }),
            'dest_city': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '',
            }),
            'max_transhipments': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '',
            }),
            # 'depart_date': DatePickerInput(),

            'depart_date': DateInput(format='%d-%m-%Y', attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'return_date': DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'num_adults': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '1',
            }),
            'num_children': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0',
            }),

            'telegr_acc': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['depature_city'].label = 'Откуда'
        self.fields['dest_city'].label = 'Куда'
        # self.fields['oneway_flight'].label = 'В один конец'
        self.fields['max_transhipments'].label = 'Пересадок не более'
        self.fields['depart_date'].label = 'Дата вылета'
        self.fields['return_date'].label = 'Дата возвращения'
        self.fields['return_date'].required = False
        self.fields['num_adults'].label = 'Взрослых'
        self.fields['num_children'].label = 'Детей'
        self.fields['num_children'].required = False
        self.fields['luggage'].label = 'Багаж'
        self.fields['telegr_acc'].label = 'Телеграм аккаунт'

    def clean_depature_city(self):
        depature_city = self.cleaned_data['depature_city']
        if not CityCode.objects.filter(city_rus=depature_city):
            raise ValidationError('Город вылета не найден!')
        return depature_city

    def clean_dest_city(self):
        dest_city = self.cleaned_data['dest_city']
        if not CityCode.objects.filter(city_rus=dest_city):
            raise ValidationError('Город назначения не найден!')
        return dest_city

    def clean_depart_date(self):
        if self.cleaned_data['depart_date'] < datetime.date.today():
            raise ValidationError('Дата вылета уже прошла.')
        return self.cleaned_data['depart_date']

    def clean_return_date(self):
        if self.cleaned_data['return_date'] is not None:
            if self.cleaned_data['return_date'] < datetime.date.today():
                raise ValidationError('Дата возвращения уже прошла.')
            if self.cleaned_data['return_date'] < self.cleaned_data['depart_date']:
                raise ValidationError('Дата возвращения ранее даты вылета.')

        return self.cleaned_data['return_date']

    def clean_max_transhipments(self):
        if 0 > self.cleaned_data['max_transhipments'] > 3:
            raise ValidationError('От 0 до 3 пересадок')
        return self.cleaned_data['max_transhipments']

    def clean_num_adults(self):
        if self.cleaned_data['num_adults'] < 1 or self.cleaned_data['num_adults'] > 10:
            raise ValidationError('Не менее 1 и не более 10 взрослых пассажиров.')
        return self.cleaned_data['num_adults']

    def clean_num_children(self):
        if self.cleaned_data['num_children'] < 0 or self.cleaned_data['num_children'] > 10:
            raise ValidationError('Некорректное значение в поле "Количество детей" (не более 10)')
        return self.cleaned_data['num_children']

    def clean_telegr_acc(self):
        if self.cleaned_data['telegr_acc'][0] != '@':
            raise ValidationError('Телеграм-аккаунт должен начинаться со знака "@"')
        return self.cleaned_data['telegr_acc']

    # depature = forms.CharField(min_length=2, max_length=50, strip=True, label='Откуда')
    # dest = forms.CharField(min_length=2, max_length=50, strip=True, label='Куда')
    # leave_date = forms.DateField(label='Вылет')
    # return_date = forms.DateField(label='Возвращение')
    # tranship = forms.TypedChoiceField(choices=(0, 1, 2, 3), coerce=int, empty_value=0, label='Пересадки')
    # num_pass = forms.IntegerField(min_value=1, max_value=10, label='Пассажиры')
    # luggage = forms.BooleanField(label='Багаж')
    # seat_class = forms.TypedChoiceField(choices=('эконом', 'бизнес', 'первый', 'премиум'), empty_value='эконом',                                        label='Класс')
    # telegr_acc = forms.CharField(min_length=1, max_length=50, strip=True, label='Телеграм')
