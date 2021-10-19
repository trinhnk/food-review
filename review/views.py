from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'review/home.html', {'posts': posts})

def post(request):
    # post = Post.objects.get()
    return render(request, 'review/post.html')

def create(request):
    return render(request, 'review/create.html')

def author(request):
    return render(request, 'review/author.html')
    
def login(request):
    return render(request, 'review/login.html')