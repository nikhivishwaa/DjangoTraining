from django.urls import path
from  . import views

urlpatterns = [
    path('',views.exam, name="exam"),
    path('result/',views.result, name="result"),
]