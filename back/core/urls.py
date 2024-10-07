from django.contrib import admin
from django.conf.urls import handler404, handler500, handler403
from django.shortcuts import redirect
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title = "Snippets API",
      default_version = 'v1',
      description = "Swagger for blog project",
   ),
   public = True,
   permission_classes = (permissions.IsAdminUser,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout = 0), name = 'schema-swagger-ui'),
    path('contact/', include('contact.urls')),
]

def default_error_handler(*args, **kwargs):
	return redirect('login')

handler403 = default_error_handler
handler404 = default_error_handler
handler500 = default_error_handler