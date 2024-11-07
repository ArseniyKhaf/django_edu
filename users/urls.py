from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from django.contrib.auth.views import LogoutView
from main import views

app_name = "urls"

urlpatterns = [
    path('logout/', LogoutView.as_view(template_name='users/logget_out.html'), name='logout')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
