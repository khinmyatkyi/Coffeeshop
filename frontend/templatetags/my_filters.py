from django import template
register = template.Library()

@register.filter
def sumTotal(list):
    total=0
    for l in list:
        total+=l.menu_id.price * l.qty
    return total

@register.filter
def priceTotal(l):
    total=0
    total+=l.menu_id.price * l.qty
    return total