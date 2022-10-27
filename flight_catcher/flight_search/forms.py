from django import forms
from django.core.exceptions import ValidationError
from django.forms import TextInput, DateTimeInput, CheckboxInput
from .models import Search, CityCode


class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ['depature_city', 'dest_city', 'max_transhipments', 'depart_date', 'return_date',
                  'num_adults', 'num_children', 'luggage', 'telegr_acc']


        widgets = {
            'depature_city': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '',
            }),
            'dest_city': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '',
            }),
            'max_transhipments': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '',
            }),
            'depart_date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': '',
                'type': 'date',
            }),
            'return_date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': '',
                'type': 'date',
            }),
            'num_adults': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '',
            }),
            'num_children': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '',
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

        if len(depature_city) > 40:
            raise ValidationError('Длина превышает 40 символов')
        return depature_city

    def clean_dest_city(self):
        dest_city = self.cleaned_data['dest_city']
        if not CityCode.objects.filter(city_rus=dest_city):
            raise ValidationError('Город назначения не найден!')
        return dest_city

    # depature = forms.CharField(min_length=2, max_length=50, strip=True, label='Откуда')
    # dest = forms.CharField(min_length=2, max_length=50, strip=True, label='Куда')
    # leave_date = forms.DateField(label='Вылет')
    # return_date = forms.DateField(label='Возвращение')
    # tranship = forms.TypedChoiceField(choices=(0, 1, 2, 3), coerce=int, empty_value=0, label='Пересадки')
    # num_pass = forms.IntegerField(min_value=1, max_value=10, label='Пассажиры')
    # luggage = forms.BooleanField(label='Багаж')
    # seat_class = forms.TypedChoiceField(choices=('эконом', 'бизнес', 'первый', 'премиум'), empty_value='эконом',                                        label='Класс')
    # telegr_acc = forms.CharField(min_length=1, max_length=50, strip=True, label='Телеграм')
