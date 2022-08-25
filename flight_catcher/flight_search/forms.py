from django import forms
from .models import *


class AddSearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ['depature_city', 'dest_city', 'oneway_flight', 'max_transhipment', 'arrival_date', 'return_date',
                  'num_adults', 'luggage', 'seat_class']
        widgets = {
            'depature_city': forms.TextInput(
                attrs={'min_length': 2, 'max_length': 50, 'strip': True, 'label': 'Откуда'})

        }
    # depature = forms.CharField(min_length=2, max_length=50, strip=True, label='Откуда')
    # dest = forms.CharField(min_length=2, max_length=50, strip=True, label='Куда')
    # leave_date = forms.DateField(label='Вылет')
    # return_date = forms.DateField(label='Возвращение')
    # tranship = forms.TypedChoiceField(choices=(0, 1, 2, 3), coerce=int, empty_value=0, label='Пересадки')
    # num_pass = forms.IntegerField(min_value=1, max_value=10, label='Пассажиры')
    # luggage = forms.BooleanField(label='Багаж')
    # seat_class = forms.ModelChoiceField(queryset=SeatClass.objects.all(), empty_label=None, label='Класс')
    #
    # telegr_acc = forms.CharField(min_length=1, max_length=50, strip=True, label='Телеграм')
    # phone_num = forms.CharField(min_length=10, max_length=20, strip=True, label='Телефон')
    # email = forms.EmailField()
