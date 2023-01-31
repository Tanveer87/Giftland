from django.db import models
#from user.models import order
# Create your models here.
class Product(models.Model):
    product_id=models.IntegerField(blank=True,null=True)
    product_name=models.CharField(max_length=200)
    product_price=models.FloatField(blank=True,null=True)
    product_totalstock=models.CharField(max_length=100)


    def __str__(self):
        return self.product_name

class Category(models.Model):
    category_id=models.IntegerField(blank=True,null=True)
    category_type=models.CharField(max_length=200)

    #product=models.ManyToManyField(Product)
    

    def __str__(self):
        return self.category_type        

class Review(models.Model):
    Rating=(
        ('Five Star','Five Star'),
        ('Four Star','Four Star'),
        ('Three Star','Three Star'),
        ('Two Star','Two Star'),
    )
    Comment=(
        ('Good Sevices','Good Sevices'),
        ('Can be better','Can be better'),
        ('Affordable price','Affordable price'),
        ('First delivery','First delivery'),
        ('Quality of the product is good','Quality of the product is good'),
        ('Satisfied with the product','Satisfied with the product'),
    )
    review_id=models.IntegerField(blank=True,null=True)
    review_rating=models.CharField(max_length=100,choices=Rating)
    review_comment=models.CharField(max_length=200,choices=Comment)
    
    #product=models.ManyToManyField(Product)
    
    def __str__(self):
        return self.review_comment          

class Cart(models.Model):
    Drate=(
        ('No Discount','No Discount'),
        ('25% Discount','25% Discount'),
        ('50% Discount','50% Discount'),
        ('70% Discount','70% Discount'),
    )
    Status=(
        ('Pending','Pending'),
        ('Out for delivery','Out for delivey'),
        ('Delivered','Delivered'),      
    )
    cart_id=models.IntegerField(blank=True,null=True)
    cart_status=models.CharField(max_length=100,choices=Status)
    cart_time=models.DateTimeField(auto_now_add=True)
    cart_discount=models.CharField(max_length=200,choices=Drate)

    #users=models.ForeignKey(user,on_delete=models.CASCADE,null=True,default=1)
    #orders=models.ForeignKey(order,on_delete=models.CASCADE,null=True)
    #product=models.ManyToManyField(Product)
    #users=models.ForeignKey(user,on_delete=models.SET_NULL,null=True,default=1)
    
    def __str__(self):
        return self.cart_discount                     


class ProductCategory(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,default=1)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,default=1)        
    
    # def __str__(self):
    #    return str(self.Product.product_id) + "," + str(self.Category.category_id)  

class ProductReview(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,default=1)
    review=models.ForeignKey(Review,on_delete=models.SET_NULL,null=True)
    
    # def __str__(self):
    #     return str(self.Product.product_id) + "," + str(self.Review.review_id)      

class ProductCart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,default=1)
    cart=models.ForeignKey(Cart,on_delete=models.SET_NULL,null=True)
    # def __str__(self):
    #     return str(self.Product.product_id) + "," + str(self.Cart.cart_id)    

