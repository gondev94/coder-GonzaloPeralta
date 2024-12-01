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

def tirar_dado(request):
    from datetime import datetime
    from random import randint
    tiro_de_dado = randint (1,6)
    if tiro_de_dado == 6:
        mensaje = f'Has tirado el dado y has sacado ¡{tiro_de_dado}! ¡Ganaste!'
    else:
        mensaje = f'Has tirado eldado y has sacado ¡{tiro_de_dado}! ¡Sigue intentado!'
        
    datos = {'title': 'Tiro de dados'}
    return render(request, 'core/dados.html', context=datos)