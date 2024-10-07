from rest_framework import serializers

from . import models

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = ('__all__')

    def create(self, validated_data):  
        return models.Article.objects.create(**validated_data) 
    
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        fields = ('__all__')

    def create(self, validated_data):  
        return self.Meta.model.objects.create(**validated_data) 