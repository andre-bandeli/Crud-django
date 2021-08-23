from django.urls import path, include
from .views import index, pag_login

app_name = "pages"


urlpatterns = [
    path('', index, name='index.html'),
    path('home', pag_login, name='home.html'),
]