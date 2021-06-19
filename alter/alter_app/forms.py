from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here
class RegistrationForm(UserCreationForm):
    # Overwriting constructor for password fields to comply with bootstrap (don't ask why, it only works as an overwrite)
    password1 = forms.CharField(
        label = 'Password',
        widget = forms.PasswordInput(attrs={
            'class': 'form-control'
        })
    )

    password2 = forms.CharField(
        label = 'Password',
        widget = forms.PasswordInput(attrs={
            'class': 'form-control'
        })
    )

    # Custom User registration form 
    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'id': 'RegisterUsername',
                'aria-describedby': 'UsernameHelp',
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'type': 'email',
                'id': 'RegisterEmail',
                'aria-describedby': 'RegisterEmailHelp'
            }),

            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'type': 'password',
                'id': 'RegisterPassword',
            }),

            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'type': 'password',
                'id': 'RegisterConfirmPassword'
            }),
        }
    
