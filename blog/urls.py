from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^services/', views.services, name='services'),
    url(r'^gallery/', views.gallery, name='gallery'),
    url(r'^product/', views.product, name='product'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^$', views.index, name='index'),
]
