from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('json/', views.storeJson, name='storeJson'),
    path('json2/', views.storeJsonToEachRecord, name='storeJsonToEachRecord'),
    path('json3/', views.ai_analysis_log, name='ai_analysis_log')
]