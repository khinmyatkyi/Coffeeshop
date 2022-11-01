from django.shortcuts import render,redirect
from menu.models import Label, Menu
from django.http import HttpRequest, HttpResponse
from django.core import serializers
from menu.models import Order, Order_Item

def get_categories(request:HttpRequest):
    labels = Label.objects.all().order_by('name')
    json_data = serializers.serialize('json', labels)
    return HttpResponse(json_data, content_type='application/json')


