from django.urls import path
from .views import form, create, home, edit, update, delete

app_name = "tasks"

urlpatterns = [
    path("new/", form, name="form"),
    path("create/", create, name="create"),
    path("lista/", home, name="home"),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
     path('delete/<int:pk>/', delete, name='delete'),
]