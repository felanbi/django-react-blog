from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.viewsets import ReadOnlyModelViewSet

from . import serializers,models

class ReadOnlyModelViewSetJWT(ReadOnlyModelViewSet):
    authentication_classes = [JWTAuthentication]
 
class ArticlesListView(ReadOnlyModelViewSetJWT):
    serializer_class = serializers.ArticleSerializer
    queryset = models.Article.objects.all()

class EventsListView(ReadOnlyModelViewSetJWT):
    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects.all()