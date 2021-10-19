from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'review/home.html')

def post(request):
    return render(request, 'review/post.html')

def create(request):
    return render(request, 'review/create.html')

def author(request):
    return render(request, 'review/author.html')
    
def login(request):
    return render(request, 'review/login.html')