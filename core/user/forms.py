from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','style': 'width: 100%;'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','style': 'width: 100%;'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','style': 'width: 100%;'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control','style': 'width: 100%;'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control','style': 'width: 100%;'}))
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput(attrs={'class': 'form-control','style': 'width: 100%;'}))
    born_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'date'}))
    weight = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control','style': 'width: 100%;', 'step': '0.1'}))
    height = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control','style': 'width: 100%;', 'step': '0.1'}))
    gender = forms.ChoiceField(choices=CustomUser.GENDER_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select','style': 'width: 100%;',}))
  
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name', 'username', 'email', 'password1', 'password2', 'born_date','weight','height', 'gender')


class LoginForm(AuthenticationForm):
    username = UsernameField(label="Username",widget=forms.TextInput(attrs={
        'class': 'form-control','style': 'width: 100%;'
        }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control','style': 'width: 100%;'
        }))
