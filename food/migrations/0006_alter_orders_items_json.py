# Generated by Django 4.0.1 on 2022-09-13 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_remove_orders_userid_orders_userid_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='items_json',
            field=models.JSONField(default=dict),
        ),
    ]
