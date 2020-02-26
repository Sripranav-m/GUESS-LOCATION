from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 100,required=True)
    password = forms.CharField(widget = forms.PasswordInput(),required=True)

class SignupForm(forms.Form):
    email    = forms.EmailField(required=True)
    username = forms.CharField(max_length = 100,required=True)
    password = forms.CharField(widget = forms.PasswordInput(),required=True)