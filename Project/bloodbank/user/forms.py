from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=50, help_text='Required')

    field_order = ['username', 'first_name', 'last_name', 'email', 'contact_number', 'is_blood_bank_admin',
                   'is_donor_or_receiver', 'gender', 'dob', 'address', 'city', 'state', 'blood_group',
                   'number_of_donations',
                   'data_share']

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email', 'contact_number', 'is_blood_bank_admin',
            'is_donor_or_receiver', 'gender', 'dob', 'address', 'city', 'state', 'blood_group', 'number_of_donations',
            'data_share')
