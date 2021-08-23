from django.urls import path
from .views import ListTasks

app_name = "tasks"

urlpatterns = [
    path("new/", ListTasks, name="ListTasks"),
]