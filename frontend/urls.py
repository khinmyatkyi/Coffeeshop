from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.HomeView.as_view(), name='home'),
    path('item/<int:id>', view=views.order_item, name='order_item'),
    path('cart',view=views.orderCart,name='orderCart'),    
    path('add_item/<int:id>', view=views.increaseQty, name="increaseQty"),
    path('sub_item/<int:id>',view=views.decreaseQty, name='decreaseQty'),
    path('ok',view=views.ok,name='ok'), 
]
