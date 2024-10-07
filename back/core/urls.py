from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.conf import settings
from django.conf.urls import handler404, handler500, handler403
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('contact/', include('contact.urls')),
	path('api/', include('api.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

def default_error_handler(*args, **kwargs):
	return redirect('login')

handler403 = default_error_handler
handler404 = default_error_handler
handler500 = default_error_handler