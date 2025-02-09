from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserResgisterForm(UserCreationForm):
    email = forms.EmailField(max_length=50, required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
