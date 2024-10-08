from django.urls import path

from main import views

urlpatterns = [
    path('', views.index),
    path("prof/", views.profil)
]
