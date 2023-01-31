from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from .forms import Profileform
from .models import Profile
from ProductInfo.models import Cart
from .forms import reg_form

# Create your views here.

# def Registerpage(request):
#     form = UserCreationForm()
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user=form.save()
#             cart= Cart(user=user)
#             cart.save()
#             form.save()
#             return redirect('/')
#     context={
#         'form':form,
#     }
#     return render(request,'registration/register.html',context)


def Registerpage(request):
    form = reg_form()

    if request.method == "POST":
        form = reg_form(request.POST)

        if form.is_valid():
            user = form.save()
            cart = Cart(user=user)
            cart.save()
            form.save()
            return redirect('/')

    context = {
        'form': form,
    }
    return render(request, 'registration/register.html', context)


@login_required
def CreateProfile(request):
    form = Profileform()
    if request.method == "POST":
        form = Profileform(request.POST, request.FILES)

    if form.is_valid():
        profile_object = form.save(commit=False)
        profile_object.user = request.user
        profile_object.save()
        return redirect('/')
    try:
        value = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        value = '0'
    context = {
        'val': value,
        'form': form,
    }
    return render(request, 'UserManagement/create_profile.html', context)


def ViewProfile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = print("Please complete your Profile to view")
    context = {
        'profile': profile,
    }
    return render(request, 'UserManagement/view_profile.html', context)
