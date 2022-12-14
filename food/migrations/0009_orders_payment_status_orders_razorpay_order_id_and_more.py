# Generated by Django 4.1.1 on 2022-10-02 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0008_rename_unique_restaurent_id_product_unique_product_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='payment_status',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='razorpay_order_id',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='razorpay_payment_id',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='razorpay_signature',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]
