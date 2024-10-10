from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from main import views

urlpatterns = [
    path('', views.index),
    path("prof/", views.profil)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)