from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Cart)
admin.site.register(ProductCategory)
admin.site.register(ProductReview)
admin.site.register(ProductCart)