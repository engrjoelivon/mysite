from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def home(request):
    return  HttpResponse("welcome to my page")


def ret_json(request):
    data = {'foo': 'bar', 'hello': 'world'}
    return HttpResponse(json.dumps(data), content_type='application/json')