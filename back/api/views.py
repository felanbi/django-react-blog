from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.viewsets import ReadOnlyModelViewSet
from django.conf import settings
from django.http.request import HttpRequest
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

from . import serializers,models

# @method_decorator(never_cache, name='dispatch')
class ReadOnlyModelViewSetJWT(ReadOnlyModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
 
class ArticlesListView(ReadOnlyModelViewSetJWT):
    serializer_class = serializers.ArticleSerializer
    queryset = models.Article.objects.all()

    def dispatch(self, request, *args, **kwargs):
        # print(request.META['Authorization'])
        print(request.headers)
        return super().dispatch(request, *args, **kwargs)

class EventsListView(ReadOnlyModelViewSetJWT):
    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects.all()