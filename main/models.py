from django.db import models

# Create your models here.


class ObraFecha(models.Model):

    obra_fecha = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200, default=1)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Categoría"

    def __str__(self):
        return self.obra_fecha



class Obra(models.Model):
    obra_title = models.CharField(max_length=200)
    obra_content = models.TextField()
    obra_published = models.DateTimeField('date published')
    #https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.ForeignKey.on_delete
    obra_fecha = models.ForeignKey(ObraFecha, default=1, verbose_name="Fecha", on_delete=models.SET_DEFAULT)
    obra_slug = models.CharField(max_length=200, default=1)
    def __str__(self):
        return self.obra_title