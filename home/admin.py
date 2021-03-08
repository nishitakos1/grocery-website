from django.contrib import admin
from .models import GroceryItem, Orders, Orderupdate, Quantity

# Register your models here.
admin.site.register(GroceryItem)
admin.site.register(Orders)
admin.site.register(Orderupdate)
admin.site.register(Quantity)
