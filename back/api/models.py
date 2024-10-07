from django.db import models

class Article(models.Model):
    publication_date = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length = 255, null = False)
    content = models.TextField(null = False)
    image = models.ImageField(null = False, upload_to = 'articles')

class Event(models.Model):
    publication_date = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length = 255, null = False)
    start_date = models.DateTimeField(null = True)
    end_date = models.DateTimeField(null = True)
    content = models.TextField(null = False)
    image = models.ImageField(null = False, upload_to = 'events')
