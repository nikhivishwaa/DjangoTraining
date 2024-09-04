from django.urls import path
from mlapp import views

app_name = 'mlapp'

urlpatterns = [
    path('predict/', views.predict, name='predict'),
    path('result/', views.result, name='result'),
]