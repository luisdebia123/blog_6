from django.urls import path
from .import views

app_name='app_blog_6' 

urlpatterns = [    
    path('', views.index, name='index'),
    path('generales/', views.generales, name='generales'),
    path('programacion/', views.programacion, name='programacion'),
    path('tecnologia/', views.tecnologia, name='tecnologia'),
    path('tutoriales/', views.tutoriales, name='tutoriales'),
    path('videojuegos/', views.videojuegos, name='videojuegos'),
    path('post/', views.post, name='post'),
    path('<slug:slug>/',views.detalle_post, name='detalle_post'),
]


