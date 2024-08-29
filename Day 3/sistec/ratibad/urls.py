from django.urls import path
from ratibad import views

urlpatterns = [
    path('',views.home, name='rhome'),
    path('about/',views.about, name='rabout'),
    path('help/',views.help, name='rhelp'),
    path('contact/',views.contact, name='rcontact'),
]
