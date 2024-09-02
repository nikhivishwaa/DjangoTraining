from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def home(request):
    # template = loader.get_template('index.html')
    template = loader.get_template('base.html')
    res = template.render()
    
    return HttpResponse(res)

def about(request):
    template = loader.get_template('index.html')
    res = template.render()
    
    return HttpResponse(res)

def help(request):
    template = loader.get_template('help.html')
    res = template.render()
    
    return HttpResponse(res)

def python(request):
    template = loader.get_template('python.html')
    res = template.render()
    
    return HttpResponse(res)

def ml(request):
    template = loader.get_template('ml.html')
    res = template.render()
    
    return HttpResponse(res)

def flutter(request):
    template = loader.get_template('flutter.html')
    res = template.render()
    
    return HttpResponse(res)

def dbms(request):
    template = loader.get_template('dbms.html')
    res = template.render()
    
    return HttpResponse(res)

def datascience(request):
    template = loader.get_template('datascience.html')
    res = template.render()
    
    return HttpResponse(res)
