from django.shortcuts import render
from .models import *
from django.forms import ModelForm
from .form import AddProduct
from .form import AddCategory
from .form import AddReview
from .form import AddCart
# Create your views here.
def Show_Product(request):
    product_info=Product.objects.all()
    category_info=Category.objects.all()
    review_info=Review.objects.all()
    cart_info=Cart.objects.all()
    #productreview_info=ProductReview.objects.all()
    context={
        'product_info':product_info,
        'category_info':category_info,
        'review_info':review_info,
        'cart_info':cart_info,
        #'productreview_info':productreview_info,
    }
    return render(request,'product.html',context)

def ProductAdd(request):
    form=AddProduct()
    massage = "Add Product"
    if request.method=="POST":
        form =AddProduct(request.POST)
        massage = "Product is not valid"
        if form.is_valid():
            form.save()
            form=AddProduct()
            massage = "Successfully added Product" 

    context={
        "form":form,
        'massage':massage,
    }
    return render(request,'product2.html',context)                    



def CategoryAdd(request):
    form=AddCategory()
    massage = "Add Category"
    if request.method=="POST":
        form =AddCategory(request.POST)
        massage = "Category is not valid"
        if form.is_valid():
            form.save()
            form=AddCategory()
            massage = "Successfully added Category"
             

    context={
        "form":form,
        "massage":massage,
    }
    return render(request,'category.html',context)     


def ReviewAdd(request):
    form=AddReview()
    massage = "Add a Review"
    if request.method=="POST":
        form =AddReview(request.POST)
        massage = "Something went worng"
        if form.is_valid():
            form.save()
            form=AddReview()
            massage = "Successfully added Review" 

    context={
        "form":form,
        "massage":massage,
    }
    return render(request,'review.html',context)   


def CartAdd(request):
    form=AddCart()
    massage = "Add into Cart"
    if request.method=="POST":
        form =AddCart(request.POST)
        massage = "Something went worng"
        if form.is_valid():
            form.save()
            form=AddCart()
            massage = "Successfully added Cart" 

    context={
        "form":form,
        "massage":massage,
    }
    return render(request,'cart.html',context)     