from django.urls import path
from gn import views

urlpatterns = [
    path('',views.home,name='gn'),
    path('about/',views.about,name='about'),
]