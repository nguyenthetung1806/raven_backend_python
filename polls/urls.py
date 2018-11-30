from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('polls/', views.index, name='index')
    path('adi', views.index, name='index')
]