

# Create your views here.
from django.shortcuts import render



def index(request):
        return render(request, 'blog/index.html', {})


def contact(request):
        return render(request, 'blog/contact.html', {})


def product(request):
        return render(request, 'blog/product.html', {})


def gallery(request):
        return render(request, 'blog/gallery.html', {})


def services(request):
        return render(request, 'blog/services.html', {})