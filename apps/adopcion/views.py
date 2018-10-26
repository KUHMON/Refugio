from django.shortcuts import render

from django.http import HttpResponse

def index_adopcion(request):
    return HttpResponse("pagina de adopcion")

