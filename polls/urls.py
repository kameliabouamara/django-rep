#after creating the first view we needt to map it to a 
#URL=adresses or uniform Resourse Locator
#this is a URLconf 

from django.urls import path
from . import views

urlpatterns =[
    path('',views.index, name='index'),
]