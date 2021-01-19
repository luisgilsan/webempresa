from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):

    title = models.CharField(max_length=100,verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True,verbose_name="Actualizado")

    class Meta:
        ordering = ["created"]
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.title

class Post(models.Model):

    title = models.CharField(max_length=200,verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de Publicación",default=timezone.now)
    image = models.ImageField(verbose_name="Imagen",upload_to="blog",null=True,blank=True)
    author = models.ForeignKey(User,verbose_name="Autor",on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category,verbose_name="Categorias",related_name='get_post')
    created = models.DateTimeField(auto_now_add=True,verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True,verbose_name="Actualizado")

    class Meta:
        ordering = ["created"]
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"

    def __str__(self):
        return self.title 
