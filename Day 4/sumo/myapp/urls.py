from django.urls import path
from myapp import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('help/', views.help, name="help"),
    path('dbms/', views.dbms, name="dbms"),
    path('flutter/', views.flutter, name="flutter"),
    path('ml/', views.ml, name="ml"),
    path('datascience/', views.datascience, name="datascience"),
    path('python/', views.python, name="python"),
]
