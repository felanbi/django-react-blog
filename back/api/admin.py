from django.contrib import admin

from . import models

admin.site.register((
    models.Article,
    models.Event
))
