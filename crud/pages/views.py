
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def pag_login(request):
    if request.user.id:
        return render(request, 'home.html')

