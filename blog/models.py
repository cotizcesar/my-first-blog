from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User') #Autor apegado a las claves foreneas de User que viene por default en Django.
    title = models.CharField(max_length = 200) #Titulo con maximo 200 caracteres.
    text = models.TextField() #Texto con un TextField ilimitado
    created_date = models.DateTimeField(default = timezone.now) #Fecha de Creacion con dia, mes y a;o. No entiendo lo del timezone.now (pendiente de buscar que es exactamente, mas que todo su formato)
    published_date = models.DateTimeField(blank = True, null = True) #Fecha de Publicacion  con dia, mes y a;o, puede star en blanco y puede ser null tambien.

    def publish(self):
        self.published_date = timezone.now() #Se que tiene el timezone y aplica la fecha al modelo Post, pero no se exactamente que significa.
        self.save() #Esta es la forma de guardar el Post.
    
    def __str__(self):
        return self.title #Con esto retorno el objeto como un String para poder leerlo mejor y no como un objeto.