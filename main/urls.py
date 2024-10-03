from django.urls import path

from main import views

urlpatterns = [
    path('', views.main),
    path("prof/", views.profil)
]
