from operator import contains
from tkinter.messagebox import NO
from django.shortcuts import render, redirect
from django.http import HttpRequest
from menu.models import Label, Menu, Order, Order_Item
from django.views.generic import View
from django.core.paginator import Paginator


list = []

class HomeView(View):
    def get(self, request:HttpRequest):
        menus = []
        if 'category' in request.GET:
            menus = Menu.objects.all().filter(label_id = request.GET['category'])
        elif 'q' in request.GET:
            menus = Menu.objects.filter(name__startswith=request.GET['q'])
        else:
            menus = Menu.objects.all()

        paginator = Paginator(menus, 4)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)

        return render(request, 'frontend/index.html',{'page':page,'list':list,})

def order_item(request:HttpRequest, id):
    #list=[]
    item = Order_Item()
    item.menu_id = Menu.objects.get(pk=id)
    order = Order.objects.last()
    item.order_id = order.id + 1 
    
    if len(list) != 0:
        for l in list:
            if l.menu_id.id == item.menu_id.id:
                l.qty += 1
                return redirect('home')
            
    item.qty = 1
    list.append(item)  
    #for pagination
    menus = Menu.objects.all()
    paginator = Paginator(menus, 4)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return redirect('home')

def orderCart(request:HttpRequest):
    if request.method == 'POST':
        customername = request.POST['customername']
        address = request.POST['address']
        phone = request.POST['phone']
        total=0
        for l in list:
            total += l.menu_id.price * l.qty
        order = Order(customer_name=customername,address=address,phone=phone,total_paid=total)
        order.save()
        for l in list:
            order_item = Order_Item(order_id=l.order_id, menu_id=l.menu_id, qty=l.qty)
            order_item.save()
        return render(request, 'fragment/thankview.html',{'order':order,'list':list,})
    if len(list) == 0:
        return redirect('home')
    else:
        return render(request, 'fragment/cart.html',{'list':list,})

def ok(request:HttpRequest):
    list.clear()
    return redirect('home')


def sumTotal(list):
    total=0
    for l in list:
        total += l.menu_id.price * l.qty
    return total


def increaseQty(request:HttpRequest,id):
    item = Order_Item()
    item.menu_id = Menu.objects.get(pk=id)
    for l in list:
        if l.menu_id.id == item.menu_id.id:
            l.qty +=1
            return redirect('orderCart')
    return redirect('orderCart')

def decreaseQty(request:HttpRequest,id):
    item = Order_Item()
    item.menu_id = Menu.objects.get(pk=id)
    for l in list:
        if l.menu_id.id == item.menu_id.id:
            if l.qty == 1:
                list.remove(l)
                if len(list) == 0:
                    return redirect('home')
            else: 
                l.qty -=1
            return redirect('orderCart')
    return redirect('orderCart')

