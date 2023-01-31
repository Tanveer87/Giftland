from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Review(models.Model):
    RatingStar=(
        ('*','*'),
        ('**','**'),
        ('***','***'),
        ('****','****'),
        ('*****','*****'),
    )

    rating=models.CharField(max_length=10,choices=RatingStar,default='***')
    comment=models.TextField(blank=True,null=True)

    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.rating



class Product(models.Model):
    p_id=models.IntegerField(default=0)
    p_name=models.CharField(max_length=100)
    p_price=models.FloatField(blank=True)
    description=models.TextField(blank=True)
    category=models.CharField(max_length=100)
    p_image=models.ImageField(upload_to='product/images')
    #file = models.FileField(upload_to='products/files/', blank=True, null=True, default='products/files/default.pdf')

    reviews = models.ManyToManyField(Review)
    
    def __str__(self):
        return self.p_name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    product = models.ManyToManyField(Product)


    created_date= models.DateTimeField(auto_now_add= True ,auto_now=False)
    update_date=models.DateTimeField(auto_now_add=False ,auto_now=True)

    def __str__(self):
        return self.user.username 

class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)

    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Delivering', 'Delivering'),
        ('Completed', 'Completed')
    )

    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Pending')

    PAYMENT_OPTION=(
        ('Bkash','Bkash'),
        ('Rocket','Rocket'),
        ('Cash on delivery','Cash on delivery'),
    )

    payment_method= models.CharField(max_length=100,choices=PAYMENT_OPTION,default='Cash on delivery')

    paid = models.BooleanField(default=False)

    transaction_id = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.user.username + "-" + self.product.p_name + "-" + self.status