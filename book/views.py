from django.shortcuts import render 
from django.views.generic import TemplateView 
# Create your views here. 
from django.http import HttpResponse 
def index(request): 
    return HttpResponse("Bienvenidos a mi sitio de libros") 

class IndexPageView(TemplateView): 
    template_name = "index.html" 

class LibroPageView(TemplateView): 
    template_name = "book.html" 