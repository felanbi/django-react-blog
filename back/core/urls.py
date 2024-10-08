from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls')),
	path('api/', include('api.urls')),

    path('', views.HomeView.as_view(), name = 'home'),
    path('articles/', views.HomeView.as_view(), name = 'articles'),
    path('events/', views.HomeView.as_view(), name = 'events'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)