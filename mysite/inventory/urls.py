from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'), #This will process after processing urls.py in root folder
    path('/about',views.about,name='about')
]