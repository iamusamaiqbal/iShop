from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.utils.datetime_safe import datetime


class Category(models.Model):
    cat_Name = models.CharField(max_length=20, default="none")

    def __str__(self):
        return self.cat_Name


class SubCat(models.Model):
    # Foreign Key
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    sub_cat_name = models.CharField(max_length=20, default="sub cat")
    cat_Image = models.URLField(max_length=150, default="Null")

    def __str__(self):
        return self.sub_cat_name


class Product(models.Model):
    # Foreign Key
    sub_cat = models.ForeignKey(SubCat, on_delete=models.CASCADE, default=None, null=True)

    product_Name = models.CharField(max_length=20, default="product name")
    product_Price = models.IntegerField(default=0)
    product_Image = models.URLField(max_length=150, default="Null")
    product_Stock = models.BooleanField(default=True)
    product_Time = models.DateTimeField(auto_now=True)
    product_Description = models.TextField(default="description")

    def __str__(self):
        return self.product_Name


class Order(models.Model):
    # Foreign Key
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None, null=True)

    order_Status = models.CharField(max_length=20, default="Success")
    total_Amount = models.FloatField(max_length=10, default=0.0)
    order_Shipping_Charges = models.FloatField(max_length=10, default=0.0)
    order_Tax = models.FloatField(max_length=10, default=0.0)
    order_Mobile = models.IntegerField(default=0)
    order_Address = models.CharField(max_length=50, default="order Address")
    order_Country = models.CharField(max_length=20, default="Pakistan")
    order_PayMethod = models.CharField(max_length=20, default="COD")
    order_TrackId = models.IntegerField(default=0)

    def __str__(self):
        return self.order_Status


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(default=0)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
