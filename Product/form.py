from django import forms
from .models import Product
from .models import Category
from .models import Review
from .models import Cart

class AddProduct(forms.ModelForm):
    class Meta:
        model=Product
        fields = '__all__'

class AddCategory(forms.ModelForm):
    class Meta:
        model=Category
        fields = ('category_id','category_type')

class AddReview(forms.ModelForm):
    class Meta:
        model=Review
        fields = ('review_rating','review_comment')    

class AddCart(forms.ModelForm):
    class Meta:
        model=Cart
        fields = '__all__'          