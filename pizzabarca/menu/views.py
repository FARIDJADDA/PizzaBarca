from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

# Create your views here.

def index(request):
    '''pizzas = Pizza.objects.all()
    pizzas_name_and_price = [pizza.name + " : " + str(pizza.price) + "€" for pizza in pizzas]
    display_pizzas = ", ".join(pizzas_name_and_price)
    return HttpResponse(f"Les pizzas : {display_pizzas}")'''
    pizzas = Pizza.objects.all().order_by('price')
    return render(request, 'menu/index.html', {'pizzas': pizzas} )