from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone_number',
                  'city', 'street', 'house_number', 'apartment_number']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'phone_number': 'Телефон',
            'city': 'Город',
            'street': 'Улица',
            'house_number': 'Номер дома',
            'apartment_number': 'Номер квартиры',
        }