# Generated by Django 3.0.9 on 2020-09-19 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_productcart_productcategory_productreview'),
        ('user', '0004_delivery_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Product.Cart'),
        ),
    ]