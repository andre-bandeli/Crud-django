from django.urls import path, include
from .views import index

app_name = "pages"


urlpatterns = [
    path('', index, name='index.html'),
]