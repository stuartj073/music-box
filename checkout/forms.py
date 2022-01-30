from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'surname', 'email', 'phone_number', 
                  'street_address1', 'street_address2', 'town_or_city', 
                  'county', 'country', 'postcode',)

    def __init__(self, *args, **kwargs):
        """
        Create placeholders for OrderForm fields
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'surname': 'Surname',
            'email': 'Email',
            'phone_number': 'phone_number',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'town_or_city': 'Town or City',
            'county': 'County',
            'country': 'Country',
            'postcode': 'Postcode',
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder