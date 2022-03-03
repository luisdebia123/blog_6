
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

import random
import csv
from django.contrib import messages 
#from django.contrib.messages.views import SuccessMessage
from functools import wraps
from urllib.parse import urlparse
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.core.exceptions import PermissionDenied
from django.shortcuts import resolve_url
from django.shortcuts import reverse, redirect
from django.utils.http import urlencode
from django import forms

from django.db.models import Q
from django.core.paginator import Paginator

from app_blog_6.models import Post, Autor, Categoria

#from .forms import  CustomUserCreationForm (sólo si esta creado en el forms.py)
#from .models import Actor, Pelicula (sólo si estan creados en el models.py)

#from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#from django.views.generic.edit import CreateView, UpdateView, DeleteVie





# Create your views here.


def index(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(estado=True)
    if queryset: 
        posts = Post.objects.filter(
            Q(titulo__icontains=queryset) | 
            Q(description__icontains=queryset)
        ).distinct()

    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'posts': posts}
    return render(request,'app_blog_6/index.html', context)





def detalle_post(request,slug):
    # post = Post.objects.get(slug = slug)
    post = get_object_or_404(Post,slug = slug)
    context = {'detalle_post': post}
    return render(request,'app_blog_6/post.html', context)


def generales(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(estado=True,categoria = Categoria.objects.get(nombre__iexact = 'General'))
    
    if queryset: 
        posts = Post.objects.filter(
            Q(titulo__icontains=queryset) | 
            Q(description__icontains=queryset)
        ).distinct()

    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'posts': posts}
    return render(request,'app_blog_6/generales.html', context)


def programacion(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(estado=True,categoria = Categoria.objects.get(nombre__iexact = 'Programación'))
    
    if queryset: 
        posts = Post.objects.filter(
            Q(titulo__icontains=queryset) | 
            Q(description__icontains=queryset)
        ).distinct()

    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'posts': posts}
    return render(request,'app_blog_6/programacion.html', context)


def tecnologia(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(estado=True,categoria = Categoria.objects.get(nombre__iexact = 'Tecnología'))
    
    if queryset: 
        posts = Post.objects.filter(
            Q(titulo__icontains=queryset) | 
            Q(description__icontains=queryset)
        ).distinct()

    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'posts': posts}
    return render(request,'app_blog_6/tecnologia.html', context)


def tutoriales(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(estado=True,categoria = Categoria.objects.get(nombre__iexact = 'Tutoriales'))
    
    if queryset: 
        posts = Post.objects.filter(
            Q(titulo__icontains=queryset) | 
            Q(description__icontains=queryset)
        ).distinct()

    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'posts': posts}
    return render(request,'app_blog_6/tutoriales.html', context)


def videojuegos(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(estado=True,categoria = Categoria.objects.get(nombre__iexact = 'Video Juegos'))
    
    if queryset: 
        posts = Post.objects.filter(
            Q(titulo__icontains=queryset) | 
            Q(description__icontains=queryset)
        ).distinct()

    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'posts': posts}
    return render(request,'app_blog_6/videojuegos.html', context)


def post(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(estado=True,categoria = Categoria.objects.get(nombre__iexact = 'Post'))
    
    if queryset: 
        posts = Post.objects.filter(
            Q(titulo__icontains=queryset) | 
            Q(description__icontains=queryset)
        ).distinct()

    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'posts': posts}
    return render(request,'app_blog_6/post.html', context)