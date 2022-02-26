from django import forms
from checkout.models import Order
from .models import Users


class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Create placeholders for OrderForm fields
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_email': 'Email',
            'default_phone_number': 'phone_number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_town_or_city': 'Town or City',
            'default_county': 'County',
            'default_postcode': 'Postcode',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = False
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
