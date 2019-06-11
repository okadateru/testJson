from django.shortcuts import render
from .models import APIResponse, NewAPIResponse
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from .forms import APIResponseForm


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

    # f = APIResponseForm(request.POST, instance=data)
    # f.save()
    # string = json.dumps(data, indent=4)


    return render(request, 'openNotify/index.html', {'data': data})


# Create your views here.
#
# def my_django_view(request):
#     if request.method == 'POST':
#         r = requests.post('http://127.0.0.1:8000/api/test/', data=request.POST)
#     else:
#         r = requests.get('http://127.0.0.1:8000/api/test/', data=request.GET)
#
#     if r.status_code == 201 and request.method == 'POST':
#         data = r.json()
#         testsave_attrs = {
#             "book": data["book"],
#         }
#         testsave= T1.objects.create(**testsave_attrs)
#         return HttpResponse(r.text)
#     elif r.status_code == 200:  # GET response
#         return HttpResponse(r.json())
#     else:
#         return HttpResponse('Could not save data')
#

#######
# def storeJson(request):
#     if request.POST:
#         book_form = BookForm(request.POST)
#     author_form = AuthorForm(request.POST)
#     if (book_form.is_valid() and author_form.is_valid()):
#         log.debug("test....")
#     book = book_form.save()
#     author = author_form.save()
#     author.book = book
#     author.save()
#
#     return redirect('/index/')
#     else:
#     book_form = BookForm()
#     author_form = AuthorForm()
#     return render_to_response('addbook.html', {'form': book_form, 'form': author_form},
#                               context_instance=RequestContext(request))