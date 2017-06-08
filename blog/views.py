from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {}) # Desde mysite/urls.py > blog/urls.py > hasta blog/views.py: Me dice esta funcion que cuando reciba un request me va a enviar a un template en especifico dentro de blog/template/blog/post_list.html, lo que esta en {} no se que significa.