from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [   
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('faqs', views.faqs, name='faqs'),
    path('contact', views.contact, name='contact'),
    path('registration', views.registration, name='registration'),
    path('choice', views.choice, name='choice'),
    path('seat', views.seat, name='seat'),
    path('apply', views.apply, name='apply'),
    path('apply2', views.apply2, name='apply2'),
    path('success', views.success, name='success'),
]