from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def home(request):
  return render(request, 'home2.html')

def members(request):
  return render(request, 'all_members.html')

def mis_denuncias(request):
  return render(request, 'mis_denuncias.html')

def login(request):
  return render(request, 'login.html')

def signin(request):
  return render(request, 'signin.html')

def quiensomos(request):
  return render(request, 'quiensomos.html')

def comod(request):
  return render(request, 'comod.html')
