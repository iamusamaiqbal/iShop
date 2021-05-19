from django.contrib import admin
from mainApp.models import *

# Register your models here.

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(SubCat)
admin.site.register(Cart)
admin.site.register(CartItem)
