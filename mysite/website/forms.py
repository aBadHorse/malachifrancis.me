from django import forms

class LoginForm(forms.Form):
    user_name = forms.CharField(label = 'User Name', max_length=16)
    user_password = forms.CharField(label = 'Password', max_length=32)
