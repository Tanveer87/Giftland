from django import forms
from .models import  Admin
class AddAdmin(forms.ModelForm):
    class Meta:
        model=Admin
        fields = '__all__'