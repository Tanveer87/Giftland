from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile
from django.contrib.auth.models import User

class reg_form(UserCreationForm) :
    class Meta :
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class Profileform(forms.ModelForm):
    class Meta:
        model = Profile
        fields= ('name','Picture_Picture','Phone') 