from django.db import models
from Product.models import Cart
# Create your models here.


class user(models.Model):
    u_id = models.BigIntegerField(blank=True)
    u_name = models.CharField(max_length=100, blank=True)
    u_email = models.EmailField(max_length=50, blank=True)
    u_password = models.CharField(max_length=50, blank=True)
    u_address = models.CharField(max_length=200, blank=True)
    u_phone_no = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return str(self.id)


class order(models.Model):
    o_id = models.BigIntegerField(blank=True)
    o_status = models.CharField(max_length=200, blank=True)
    o_date = models.DateTimeField(auto_now_add=True)

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)

    user = models.ForeignKey(
        user, on_delete=models.CASCADE, default=1, null=True)

    def __str__(self):
        return str(self.o_id)


class payment(models.Model):
    payment_id = models.BigIntegerField(blank=True)
    payment_type = models.CharField(max_length=200, blank=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2)

    user = models.ForeignKey(
        user, on_delete=models.SET_NULL, default=1, null=True)

    def __str__(self):
        return str(self.payment_id)


class delivery(models.Model):
    delivery_code = models.BigIntegerField(blank=True)

    order = models.ForeignKey(
        order, on_delete=models.CASCADE, default=1, null=True)

    def __str__(self):
        return str(self.delivery_code)
