from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

from . import views

schema_view = get_schema_view(
   openapi.Info(
      title = "Snippets API",
      default_version = 'v1',
      description = "Swagger for API project",
   ),
   public = True,
)

router = DefaultRouter()

router.register('articles', views.ArticlesListView, basename = 'articles')
router.register('events', views.EventsListView, basename = 'events')

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout = 0), name = 'docs'),
    path('token/', TokenObtainPairView.as_view(), name = 'access'),
    path('token/refresh/', TokenRefreshView.as_view(), name = 'refresh'),
    path('', include(router.urls)),
]
