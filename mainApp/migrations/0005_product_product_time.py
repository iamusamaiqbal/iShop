# Generated by Django 3.2 on 2021-05-08 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_alter_cartitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_Time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
