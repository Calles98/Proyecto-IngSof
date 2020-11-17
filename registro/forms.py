from django import forms
from django.contrib.auth.models import User
from registro.models import UserProfileInfo

class UserForm(forms.ModelForm):


    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Correo Electrónico',
            'password': 'Contraseña'
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. algo@unison.mx'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),


        }
