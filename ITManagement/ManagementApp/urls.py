from django.contrib import admin
from django.urls import path    
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('machines/', views.machine_list, name='machine_list'),
    path('machines/add/', views.machine_add, name='machine_add'),
    path('machines/<pk>/', views.machine_detail, name='machine_detail'),
    path('machines/<pk>/delete/', views.machine_delete, name='machine_delete'),
    path('infrastructures/', views.infrastructure_list, name='infrastructure_list'),
    path('infrastructures/add/', views.infrastructure_add, name='infrastructure_add'),
    path('infrastructures/<pk>/', views.infrastructure_detail, name='infrastructure_detail'),
    path('infrastructures/<pk>/delete/', views.infrastructure_delete, name='infrastructure_delete'),
]
