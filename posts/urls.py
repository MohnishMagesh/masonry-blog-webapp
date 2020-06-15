from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('posts/<slug:slug>/', views.post_details, name='post_details'),
    path('search/', views.search, name='search')
]