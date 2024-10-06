from django.db import models

class Contact(models.Model):
    class Type(models.TextChoices):
        CONTACT = 'C', 'contact'
        BUG = 'B', 'bug'

    mail = models.EmailField()
    type = models.CharField(choices = Type.choices, max_length = 1)
    content = models.TextField()
    processed = models.BooleanField(default = False)
