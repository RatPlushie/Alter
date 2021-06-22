from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here
# Form used for the creation of new users
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
    

# Form used for the uploading of new art
class UploadForm(forms.Form):
    title = forms.CharField(
        label = 'title',
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'id': 'InputTitle',
            'aria-describedby': 'titleHelp',
            'placeholder': 'Fox Base'
        })
    )

    species = forms.CharField(
        label = 'Species',
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'list': 'datalistOptions',
            'id': 'speciesDataList',
            'placeholder': 'Type to search...'
        })
    )

    description = forms.CharField(
        label = 'description',
        widget = forms.Textarea(attrs={
            'class': 'form-control',
            'id': 'InputDescription',
            'rows': '4'
        })
    )

    file = forms.FileField(
        label = 'file',
        widget = forms.FileInput(attrs={
            'class': 'form-control',
            'type': 'file',
            'id': 'InputImage',
            'aria-describedby': 'imageHelp'
        })
    )

    thumbnail = forms.FileField(
        label = 'Thumbnail',
        widget = forms.FileInput(attrs={
            'class': 'form-control',
            'type': 'file',
            'id': 'InputThumbnail',
            'aria-describedby': 'thumbnailHelp'
        })
    )
