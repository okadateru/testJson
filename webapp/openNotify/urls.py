from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('json/', views.storeJson, name='storeJson')
]