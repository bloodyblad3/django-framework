from django.db import models

class Client(models.Model):
    name = models.CharField()
    email = models.EmailField()
    phone_number = models.CharField()
    adress = models.CharField()
    sign_up_date = models.DateField(auto_now_add=True)

class Product(models.Model):
    name = models.CharField()
    description = models.CharField()
    price = models.DecimalField(decimal_places=2)
    quantity = models.IntegerField()
    addition_date = models.DateField(auto_now_add=True)

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    order_sum = models.DecimalField(decimal_places=2)
    order_date = models.DateField(auto_now_add=True)