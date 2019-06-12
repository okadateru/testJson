
from django.shortcuts import render
from .models import APIResponse, NewAPIResponse, Ai_analysis_log
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
    parameters = {"lat": 50.71, "lon": -24}
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

    item = NewAPIResponse(
        message=message,
        latitude=latitude,
        longitude=longitude,
        passes=passes,
        datetime=datetime,
        altitude=altitude,
    )
    item.save()



    # items = NewAPIResponse.objects.all()
    # for item in items:
    #     item.message = message
    #     item.latitude = latitude
    #     item.longitude = longitude
    #     item.passes = passes
    #     item.datetime = datetime
    #     item.altitude = altitude
    #     item.save()

    return render(request, 'openNotify/index.html', {'data': data})
