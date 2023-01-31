from django import forms
from .models import user
from .models import order
from .models import payment
from .models import delivery


class adduser(forms.ModelForm):
    class Meta:
        model = user
        fields = '__all__'


class addorder(forms.ModelForm):
    class Meta:
        model = order
        fields = '__all__'


class addpayment(forms.ModelForm):
    class Meta:
        model = payment
        fields = '__all__'


class adddelivery(forms.ModelForm):
    class Meta:
        model = delivery
        fields = '__all__'
