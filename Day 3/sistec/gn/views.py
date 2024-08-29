from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def home(request):
    template = loader.get_template('home.html')
    response = template.render()

    return HttpResponse(response)

def about(request):
    return render(request, 'home.html')
