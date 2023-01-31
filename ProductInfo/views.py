from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Product
from .models import Order
from .models import Cart
from .models import Review
from .forms import ProductForm
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def ShowProducts(request):    
    products = Product.objects.all()
    if request.method == 'POST':
        products = Product.objects.filter(p_name__icontains = request.POST['search'])
        category = Product.objects.filter(category__icontains= request.POST['search'])
        description = Product.objects.filter(description__icontains=request.POST['search'])

        products = products | category | description

        print(products,category,description)
     
    context = {
        'products': products,
    }
    return render(request, 'ProductHtml/index.html', context)


def ProductDetails(request, product_id):
    detail = get_object_or_404(Product, id=product_id)
    context = {
        'detail': detail,
    }
    return render(request, 'ProductHtml/productdetail.html', context)

def ViewCart(request):
    cart = Cart.objects.get(user=request.user)

    total=0
    for i in cart.product.all():
        total+= i.p_price

    context={
        'cart':cart,
        'total':total,
    }

    return render (request,'ProductHtml/cart.html',context)  

@login_required
def AddtoCart(request, product_id):

    product = get_object_or_404(Product, id=product_id)
    cart = get_object_or_404(Cart, user=request.user)

    # try:
    #     cart = Cart.objects.get(user=request.user)
    # except cart.DoesNotExist:
    #     cart = Cart(user=request.user)

    cart.product.add(product)
    cart.save()

    return redirect('cart')  

@login_required
def RemovefromCart(request, product_id):

    product = get_object_or_404(Product, id=product_id)
    cart = Cart.objects.get(user=request.user)

    cart.product.remove(product)
    cart.save()

    return redirect('cart') 

@login_required
def CreateOrder(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order = Order(user=request.user, product=product)
    order.save()
    cart = get_object_or_404(Cart,user=request.user) 
    #cart = Cart.objects.get(user=request.user)
    cart.product.remove(product)
    #cart.product.add(product)
    cart.save()

    return redirect('cart')    




@login_required
def UserOrder(request) :
    
    orders = Order(user=request.user)

    try : 
        orders = Order.objects.filter(user=request.user)
        order_status = True
    except orders.DoesNotExist:
        orders = Order(user=request.user)
        order_status = False

    total = 0

    for i in orders :
        total += i.product.p_price

    context = {
        'orders' : orders,
        'order_status' : order_status,
        'total' : total
    }

    return render(request, 'ProductHtml/order.html', context)

def Payment(request, product_id) :
    product = get_object_or_404(Product, id=product_id)
    order = Order(user=request.user, product=product)

    order.transaction_id = request.POST['transaction_id']
    order.payment_options = 'Bkash'
    order.save()

    cart = Cart.objects.get(user=request.user)
    cart.product.remove(product)
    cart.save()

    return redirect('cart')

def ProductReview(request,product_id):
    review_done=False

    detail=get_object_or_404(Product,id=product_id)

    userlist = detail.reviews.filter(user=request.user)

    print(userlist,len(userlist))
    if len(userlist)!=0:
        review_done=True


    form = ReviewForm()

    if request.method=='POST':
        form = ReviewForm(request.POST)

        if form.is_valid:
            isinstance = form.save(commit=False)
            isinstance.user=request.user
            isinstance.save()

            detail.reviews.add(isinstance)
            detail.save()

            return redirect('/')

    context = {
        'detail':detail,
        'form':form,
        'review_done':review_done,
    }

    return render(request,'ProductHtml/review.html',context)
