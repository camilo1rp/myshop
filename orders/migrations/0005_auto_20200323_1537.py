# Generated by Django 3.0.4 on 2020-03-23 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_delivered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivered',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]