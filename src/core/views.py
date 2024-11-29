from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def saludar(request):
	return HttpResponse("Hola desde Django!")

def saludar_con_etiqueta(request):
    return HttpResponse("<h1>Este es el título de mi App")

def saludar_con_parametros(request, nombre: str, apellido: str):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse (f'{apellido}, {nombre}')

def index(request):
    contex = {"año" : 2024}
    return render(request, "core/index.html", contex) 