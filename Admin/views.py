from django.shortcuts import render
from .models import Admin
from django.forms import ModelForm
from .form import AddAdmin

# Create your views here.
def Show_Admin(request):
    admin_info=Admin.objects.all()
    context={
        'admin_info':admin_info,
    }
    return render(request,'admin.html',context)


def AdminAdd(request):
    form=AddAdmin()
    if request.method=="POST":
        form =AddAdmin(request.POST)
        if form.is_valid():
            form.save()
            form=AddAdmin() 

    context={
        "form":form,
    }
    return render(request,'admin2.html',context) 