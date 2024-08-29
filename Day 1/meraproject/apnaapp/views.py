from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    response = """
    <div style="width:300px;height:200px:padding:50px;margin:50px;border:2px solid red;border-radius:12px;">
    <h1> Welcome to Hell</h1>
    </div>
"""
    return HttpResponse(response)