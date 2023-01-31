from django.shortcuts import render
from user.models import*
from django.forms import ModelForm
from .form import adduser
from .form import addorder
from .form import addpayment
from .form import adddelivery

def customer(request):
    user_info = user.objects.all()
    order_info = order.objects.all()
    delivery_info = delivery.objects.all()
    payment_info = payment.objects.all()
    context = {
        'user_info': user_info,
        'order_info': order_info,
        'delivery_info': delivery_info,
        'payment_info': payment_info
    }
    return render(request, 'user.html', context)


def useradd(request):
    form = adduser()
    mss = "Add User"
    if request.method == "POST":
        form = adduser(request.POST)
        mss = "Invalid Input"
        if form.is_valid():
            form.save()
            form = adduser()
            mss = "Add Successful"

    context = {
        "form": form,
        "mss" : mss,
    }
    return render(request, 'user_into.html', context)


def orderadd(request):
    form = addorder()
    mss = "Add Order"
    if request.method == "POST":
        form = addorder(request.POST)
        mss = "Invalid Input"
        if form.is_valid():
            form.save()
            form = addorder()
            mss = "Add Successful"

    context = {
        "form": form,
        "mss" : mss,
    }
    return render(request, 'order.html', context)


def paymentadd(request):
    form = addpayment()
    mss = "Add Order"
    if request.method == "POST":
        form = addpayment(request.POST)
        mss = "Invalid Input"
        if form.is_valid():
            form.save()
            form = addpayment()
            mss = "Add Successful"

    context = {
        "form": form,
        "mss" : mss,
    }
    return render(request, 'payment.html', context)


def addDelivery(request):
    form = adddelivery()
    message = "Add Delivery"
    if request.method == "POST":
        form = adddelivery(request.POST)
        message = "Something error here"
        if form.is_valid():
            form.save()
            form = adddelivery()
            message = "Successfully Added"

    context = {
        "form": form,
        "message": message,
    }
    return render(request, 'delivery.html', context)
