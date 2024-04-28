from django.shortcuts import render
from .models import Warehouse, Goods, Customer, Sales

def text_page(request):
    warehouse = Warehouse.objects.all()
    goods = Goods.objects.all()
    customer = Customer.objects.all()
    sales = Sales.objects.all()
    context = {
        'warehouse': warehouse,
        'goods': goods,
        'customer': customer,
        'sales': sales,
    }
    return render(request, 'web/main.html', context)
