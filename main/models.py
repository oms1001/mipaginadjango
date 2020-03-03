from django.db import models

# Create your models here.

class Entrada(models.Model):
    entrada_title = models.CharField(max_length=200)
    entrada_content = models.TextField()
    entrada_published = models.DateTimeField('date published')

    def __str__(self):
        return self.entrada_title

