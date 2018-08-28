from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User

class LoginForm(forms.Form):
    user_name = forms.CharField(label = 'User Name', max_length=16)
    user_password = forms.CharField(label = 'Password', max_length=32)


class RegisterUserForm(UserCreationForm):
    #may create additional fields here if added to the custom User model
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')


#TODO add change user form for updating user info/profile
