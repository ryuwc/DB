
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'eithers'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/comment/', views.comments_create, name='comments_create'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/comments/delete/', views.comments_delete, name='comments_delete'),
    
    
    

    
]
