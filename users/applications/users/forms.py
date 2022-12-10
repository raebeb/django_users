from django import forms
from .models import User

from django.contrib.auth import authenticate

class UserRegisterForm(forms.ModelForm):
    """Form definition for UserRegister."""
    """Meta definition for UserRegisterform."""
    password = forms.CharField(
        label='Password',
        max_length=20,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
            }
        )
    )
    password_confirmation = forms.CharField(
        label='Password',
        max_length=20,required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repeat password',
            }
        )
    )

    class Meta:

        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'genre',
        )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirmation = cleaned_data.get('password_confirmation')

        if password != password_confirmation:
            self.add_error('password_confirmation', 'Passwords do not match')

class UserLoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'style': '{margin: 10px}',
            }
        )
    )
    password = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'style': '{margin: 10px}',
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Invalid username or password')
    
        return self.cleaned_data

