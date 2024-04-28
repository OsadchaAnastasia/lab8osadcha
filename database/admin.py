from django.contrib import admin
from .models import Warehouse, Goods, Customer, Sales

admin.site.register(Warehouse)
admin.site.register(Goods)
admin.site.register(Customer)
admin.site.register(Sales)