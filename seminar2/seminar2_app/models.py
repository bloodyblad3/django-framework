from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=42)
    email = models.EmailField()
    phone_number = models.CharField(max_length=16)
    adress = models.CharField(max_length=100)
    sign_up_date = models.DateField(auto_now_add=True)

class Product(models.Model):
    name = models.CharField(max_length=42)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    addition_date = models.DateField(auto_now_add=True)

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    order_sum = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField(auto_now_add=True)