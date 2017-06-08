from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date') # Nueva variable Posts filtrando todos los objetos de Post por published_date.
    return render(request, 'blog/post_list.html', {'posts': posts}) # Desde mysite/urls.py > blog/urls.py > hasta blog/views.py: Me dice esta funcion que cuando reciba un request me va a enviar a un template en especifico dentro de blog/template/blog/post_list.html, {'posts':posts} significa que va renderizar lo que esta en la variable posts (eso incluye el QuerySet)