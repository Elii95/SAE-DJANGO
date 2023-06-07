from django.contrib import admin
from django.urls import path    
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('login/', views.admin_login, name='admin_login'),
    path('logout/', views.admin_logout, name='admin_logout'),

    path('machines/', views.machine_list, name='machine_list'),
    path('machines/add/', views.machine_add, name='machine_add'),
    path('machines/<pk>/', views.machine_detail, name='machine_detail'),
    path('machines/<pk>/delete/', views.machine_delete, name='machine_delete'),
    path('infrastructures/', views.infrastructure_list, name='infrastructure_list'),
    path('infrastructures/add/', views.infrastructure_add, name='infrastructure_add'),
    path('infrastructures/<pk>/', views.infrastructure_detail, name='infrastructure_detail'),
    path('infrastructures/<pk>/delete/', views.infrastructure_delete, name='infrastructure_delete'),
    path('utilisateurs/', views.utilisateur_list, name='utilisateur_list'),
    path('utilisateurs/create/', views.utilisateur_create, name='utilisateur_create'),
    path('utilisateurs/<pk>/', views.utilisateur_detail, name='utilisateur_detail'),
    path('utilisateurs/<pk>/update/', views.utilisateur_update, name='utilisateur_update'),
    path('utilisateurs/<pk>/delete/', views.utilisateur_delete, name='utilisateur_delete'),
]
