# Generated by Django 3.1.1 on 2020-10-03 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductInfo', '0004_auto_20201003_2354'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='paid_status',
            new_name='paid',
        ),
        migrations.RemoveField(
            model_name='order',
            name='payment_options',
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('Bkash', 'Bkash'), ('Rocket', 'Rocket'), ('Cash on delivery', 'Cash on delivery')], default='Cash on delivery', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Delivering', 'Delivering'), ('Completed', 'Completed')], default='Pending', max_length=30),
        ),
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
