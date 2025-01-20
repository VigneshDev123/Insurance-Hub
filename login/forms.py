# agency/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import UserDetails

class CustomerLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class AgencyLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')

class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = [
            'first_name', 'middle_name', 'last_name', 'gender', 'phone', 
            'email', 'address', 'about_you', 'home_type', 'salary', 
            'vehicle_type', 'health_details'
        ]

