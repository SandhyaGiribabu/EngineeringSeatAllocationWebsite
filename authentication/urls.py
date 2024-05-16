from django.contrib import admin
from django.urls import path, include
from . import views 

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name="signup"),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
     # Map the root URL to the home view
    # Add more URL patterns as needed
]


