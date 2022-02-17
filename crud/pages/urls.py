from django.urls import path, include
from .views import index, login

app_name = "pages"


urlpatterns = [
    path('', index, name='index.html'),
    path('login', login, name='login.html'),
]