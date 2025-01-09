from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def home_page(request):
    return render(request, 'home.html')

