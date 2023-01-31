from django.db import models
from Product .models import Product
# Create your models here.
class Admin(models.Model):
    admin_id=models.IntegerField(blank=True,null=True)
    admin_name=models.CharField(max_length=100)
    admin_email=models.CharField(max_length=200,unique=True)
    admin_password=models.CharField(max_length=200)

    

    def __str__(self):
        return self.admin_name

class Manage(models.Model):
   product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,default=1)
   admin=models.ForeignKey(Admin,on_delete=models.SET_NULL,null=True,default=1)