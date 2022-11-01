from time import timezone
from django.db import models
from enum import unique
from django.utils import timezone
from distutils.command.upload import upload
from enum import unique

class Label(models.Model):
    name = models.CharField(max_length=60, blank=False, null=False, unique=True)
    is_active = models.BooleanField(null=False, blank=False, default=True)

    def __str__(self) -> str:
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='foods/')
    price = models.IntegerField()
    label = models.ForeignKey(Label, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Menu Name : {self.name}"

class Order(models.Model):
    customer_name = models.CharField(max_length=300)
    order_date = models.DateTimeField(blank=False, null=False, default = timezone.datetime.now)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=100)
    total_paid = models.IntegerField()

    def __str__(self) -> str:
        return f"Address : {self.address}"

class Order_Item(models.Model):
    order_id = models.IntegerField()
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    qty = models.IntegerField()

    def __str__(self) -> str:
        return f"Order Id : {self.menu_id}"
