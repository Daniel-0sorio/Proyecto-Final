"""
URL configuration for YourUSM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('members/', views.members, name='members'),
    path('mis_denuncias/', views.mis_denuncias, name='mis_denuncias'),
    path('login/', views.login, name='login'),
    path('signin/', views.signin, name='signin'),
    path('quiensomos/', views.quiensomos, name='quiensomos'),
    path('comod/', views.comod, name='comod'),

]
    #path('members/', views.members, name='members'),
    #path('members/details/<int:id>', views.details, name='details'),
    #path('testing/', views.testing, name='testing'), 