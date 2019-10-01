from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
def index(request):
    return render(request, 'index.html')

def shop(request):
    return render(request, 'shop.html')
    