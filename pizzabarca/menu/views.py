from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

# Create your views here.

def index(request):
    pizzas = Pizza.objects.all()
    pizzas_names = [pizza.name for pizza in pizzas]
    display_pizzas = ", ".join(pizzas_names)
    return HttpResponse("Les pizzas : " + display_pizzas)