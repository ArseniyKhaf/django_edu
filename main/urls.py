from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from main import views

app_name = "main"

urlpatterns = [
    path('', views.index, name='index'),
    path("prof/", views.profil),
    path("category/<slug:slug>", views.category_view, name='categories'),
    path("detail/<slug:slug>/", views.detail_view, name='detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
