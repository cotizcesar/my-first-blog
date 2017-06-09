from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'), #Viene el llamado desde mysite/urls.py > blog/urls.py y con views.post_list enviamos hasta views.py en la funcion post_list
    url(r'^post/(?P<pk>\d+)/$', views.post_detail,  name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]
