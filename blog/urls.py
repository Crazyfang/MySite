from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.blog, name='blog'),
    url(r'(?P<article_id>\d)/$', views.blog_article, name='blog_detail'),
]