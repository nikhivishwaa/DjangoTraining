from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    template = loader.get_template('index.html')
    response = template.render()

    return HttpResponse(response)

def help(request):
    template = loader.get_template('help.html')
    response = template.render()

    return HttpResponse(response)

def about(request):
    template = loader.get_template('about.html')
    response = template.render()

    return HttpResponse(response)

def contact(request):
    template = loader.get_template('contact.html')
    response = template.render()

    return HttpResponse(response)
