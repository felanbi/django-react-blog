from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.conf import settings
from django.conf.urls import handler404
from django.views.defaults import page_not_found  
from django.conf.urls.static import static
from django.core.handlers.wsgi import WSGIRequest
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('contact/', include('contact.urls')),
	path('api/', include('api.urls')),
    path('', views.HomeView.as_view(), name = 'home')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

def error_handler(request: WSGIRequest, exception = None):
    if request.path.startswith('/api'):
        return redirect('docs')
    
    return page_not_found(request, exception)

handler404 = error_handler