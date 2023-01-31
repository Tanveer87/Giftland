from django import forms
from .models import Product
from .models import Review
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('p_name', 'category', 'p_price', 'p_image','description' )



class ReviewForm(forms.ModelForm):
    class Meta:
        model= Review
        fields=('rating','comment')        