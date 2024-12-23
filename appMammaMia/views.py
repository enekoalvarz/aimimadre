from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Masa, Pizza, Ingrediente

def index(request):
    masas = Masa.objects.all()
    ingredientes = Ingrediente.objects.all()
    return render(request,"index.html", {'masas': masas, 'ingredientes':ingredientes})

def components(request):
    return render(request,"components.html")

def pizzas(request, masa_tipo):
    masa = get_object_or_404(Masa, nombre__iexact=masa_tipo)
    pizzas = Pizza.objects.filter(masa=masa)
    return render(request,"pizzas.html", {'pizzas': pizzas, 'masa': masa})

def pizza_desc(request, p_nombre):
    pizza = get_object_or_404(Pizza, nombre__iexact=p_nombre)
    return render(request, "descripcion_de_pizza.html", {'pizza':pizza})

def ingrediente_desc(request, i_nombre):
    ingrediente = get_object_or_404(Ingrediente, nombre__iexact=i_nombre)
    pizzas = Pizza.objects.filter(ingredientes__nombre__iexact=i_nombre)
    return render(request, "ingrediente.html", {'ingrediente': ingrediente, 'pizzas':pizzas})
