from django.db import models

class Warehouse(models.Model):
    warehouse_number = models.IntegerField(primary_key=True)
    warehouse_address = models.CharField(max_length=255)
    warehouse_manager = models.CharField(max_length=255)
    warehouse_phone_number = models.CharField(max_length=13)

class Goods(models.Model):
    goods_code = models.IntegerField(primary_key=True)
    goods_type = models.CharField(max_length=9)
    goods_name = models.CharField(max_length=255)
    goods_manufacturer = models.CharField(max_length=255)
    goods_warehouse_number = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    goods_warehouse_quantity = models.IntegerField()
    goods_price = models.DecimalField(max_digits=10, decimal_places=2)

class Customer(models.Model):
    customer_code = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    customer_address = models.CharField(max_length=255)
    customer_phone_number = models.CharField(max_length=13)
    contact_person = models.CharField(max_length=255)

class Sales(models.Model):
    sales_code = models.IntegerField(primary_key=True)
    sales_date = models.DateField()
    sales_customer_code = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_sales')
    sales_goods_code = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name='goods_sales')
    sales_cloth_quantity = models.IntegerField()
    discount = models.DecimalField(max_digits=5, decimal_places=2)
