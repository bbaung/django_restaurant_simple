from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .models import Menu
# Create your views here.

# def index(request):
#     return HttpResponse("Hello , welcome from home page")

def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def booking(request):
    template = loader.get_template('book.html')
    return HttpResponse(template.render())

def menu(request):
    mymenu = Menu.objects.all().values()
    template = loader.get_template('menu.html')
    context = {
        'mymenu' : mymenu,
    }
    return HttpResponse(template.render(context, request))

def display_menu_items(request,pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
        
    return render(request, 'menu_item.html', {'menu_item': menu_item})
    
