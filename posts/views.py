from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
    queryset = Post.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')
