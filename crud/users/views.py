from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse


def login(request):
    return render(request, 'login.html')