from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include('users.urls', namespace='users')),
    path('', include('main.urls', namespace="main")),
    path('auth', include('django.contrib.auth.urls')),
]
