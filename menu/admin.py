import imp
from django.contrib import admin
from .models import Label, Menu, Order, Order_Item

admin.site.register(Label)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(Order_Item)
