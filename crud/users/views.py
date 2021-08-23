from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from django.urls import reverse


def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'index.html')
