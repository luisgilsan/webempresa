from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
# Create your models here.
class Page(models.Model):

    title = models.CharField(verbose_name="Titulo",max_length=200)
    context = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden",default=0)
    created = models.DateTimeField(auto_now_add=True,verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True,verbose_name="Actualizado")
    
    class Meta:
        ordering = ["order","title"]
        verbose_name = "Página"
        verbose_name_plural = "Páginas"

    def __str__(self):
        return self.title 
