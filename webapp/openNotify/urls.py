from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #　画像のクラスを判定するAPIへ画像を送信し、データを取得する処理を行う
    path('jsonFromAIApi/', views.ai_analysis_log, name='ai_analysis_log'),

    # 動作確認用 URLs
    path('json/', viewsForOpenNotifyAPI.storeJson, name='storeJson'),
    path('json2/', viewsForOpenNotifyAPI..storeJsonToEachRecord, name='storeJsonToEachRecord'),
]