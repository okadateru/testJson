from django.shortcuts import render
from .models import APIResponse, NewAPIResponse
from django.http import HttpResponse
from django.utils.safestring import mark_safe
# from .forms import APIResponseForm


import json
import requests


def storeJson(request):

    parameters = {"lat": 40.71, "lon": -74}
    headers = {"content-type": "application/json"}
    response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters,headers=headers)
    data = json.loads(response.text) # data は 辞書型(loads()は文字列を辞書型に変換)
    print(data)

    all_objects = APIResponse.objects.all()
    for a in all_objects:
        a.jsondata=data
        a.save()

    return render(request, 'openNotify/index.html', {'data': data})



def storeJsonToEachRecord(request):
    parameters = {"lat": 40.71, "lon": -74}
    headers = {"content-type": "application/json"}
    response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters, headers=headers)
    # data は 辞書型。　(loads()はJSON文字列を辞書型に変換)
    data = json.loads(response.text)


    message = data["message"]
    latitude = data["request"]["latitude"]
    longitude = data["request"]["longitude"]
    passes = data["request"]["passes"]
    datetime = data["request"]["datetime"]
    altitude = data["request"]["altitude"]

    items = NewAPIResponse.objects.all()
    for item in items:
        item.message = message
        item.latitude = latitude
        item.longitude = longitude
        item.passes = passes
        item.datetime = datetime
        item.altitude = altitude
        item.save()

    return render(request, 'openNotify/index.html', {'data': data})


def ai_analysis_log(request):
    headers = {"content-type": "application/json"}
    parameters = {image_path:"/image/d03f1d36ca69348c51aa/c413eac329e1c0d03/test.jpg"}
    # POSTパラメータは、data引数で指定
    response = requests.post("http://example.com/", data=parameters, headers=headers)
    # data は 辞書型。　(loads()はJSON文字列を辞書型に変換)
    data = json.loads(response.text)

    image_path = data["image_path"]
    success = data["success"]
    message = data["message"]
    Class = data["request"]["Class"]
    confidence = data["request"]["confidence "]
    request_timestamp = data["request"]["request_timestamp"]
    response_timestamp = data["request"]["response_timestamp"]

    items = NewAPIResponse.objects.all()
    for item in items:
        item.image_path = image_path
        item.success = success
        item.message = message
        item.Class = Class
        item.confidence = confidence
        item.request_timestamp = request_timestamp
        item.response_timestamp = response_timestamp
        item.save()

    return render(request,'openNotify/index.html', {'data': data})