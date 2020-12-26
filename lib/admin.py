from django.contrib import admin
from .models import Item, Order, Orderitem, Shipping
# Register your models here.

admin.site.register(Item)
admin.site.register(Order)
admin.site.register(Orderitem)
admin.site.register(Shipping)
# admin.site.register(Cart)
