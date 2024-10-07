from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from . import views

schema_view = get_schema_view(
   openapi.Info(
      title = "Snippets API",
      default_version = 'v1',
      description = "Swagger for API project",
   ),
   public = True,
)

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout = 0), name = 'docs'),
    path('token/', TokenObtainPairView.as_view(), name = 'access'),
    path('token/refresh/', TokenRefreshView.as_view(), name = 'refresh'),
    path('events/', views.EventsListView.as_view({'get': 'list'}), name = 'events'),
    path('articles/', views.ArticlesListView.as_view({'get': 'list'}), name = 'articles'),   
]
