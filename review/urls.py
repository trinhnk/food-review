from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('post', views.post, name='post'),
    path('create', views.create, name='create'),
    path('author', views.author, name='author'),
    path('login', views.login, name='login'),
]
