from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'review/home.html', {'posts': posts})

def author(request):
    author = request.user
    posts = Post.objects.filter(posted_by_id=author.id)
    return render(request, 'review/author.html', {'author': author, 'posts': posts})





def post(request):
    # post = Post.objects.get()
    return render(request, 'review/post.html')

def create(request):
    return render(request, 'review/create.html')

def login(request):
    return render(request, 'review/login.html')
