from django.urls import path, include

app_name = "users"

urlpatterns = [
    path('account/', include('django.contrib.auth.urls')),
    path('account/login', include('django.contrib.auth.urls')),
    path('account/logout', include('django.contrib.auth.urls')),
    
]