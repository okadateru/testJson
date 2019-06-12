from django.shortcuts import render
from .models import APIResponse, NewAPIResponse, Ai_analysis_log
from django.http import HttpResponse
from django.utils.safestring import mark_safe

import json
import requests


def ai_analysis_log(request):
    # リクエストのタイムスタンプは暫定的に、ここで現在時刻を取得している
    request_timestamp = datetime.now()
    headers = {"content-type": "application/json", "Date": req_time }
    IMAGE_PATH = "image/d03f1d36ca69348c51aa/c413eac329e1c0d03/test.jpg"
    URLofAPI = "http://example.com/"

    parameters = {image_path:IMAGE_PATH}

    # POSTパラメータを、data引数で指定
    response = requests.post(URLofAPI, data=parameters, headers=headers)

    # レスポンスのタイムスタンプ
    response_timestamp = response.headers['date']

    # data は 辞書型。　(loads()はJSON文字列を辞書型に変換)
    data = json.loads(response.text)

    image_path = data["image_path"]
    success = data["success"]
    message = data["message"]
    classOfImage = data["estimated_data"]["class"]
    confidence = data["estimated_data"]["confidence"]


    item = Ai_analysis_log(
        image_path=image_path,
        success=success,
        message=message,
        classOfImage=classOfImage,
        confidence=confidence,
        request_timestamp=request_timestamp,
        response_timestamp=response_timestamp,
    )
    item.save()

    return render(request,'openNotify/index.html', {'data': data})