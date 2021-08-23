from django.urls import path
from .views import ListTasks, create, edit, update, home

app_name = "tasks"

urlpatterns = [
    path("home", home, name="home"),
    path("new/", ListTasks, name="ListTasks"),
    path("create/", create, name="create"),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
]