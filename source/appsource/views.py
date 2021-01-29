from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homePageRsp(req):
    return HttpResponse('<h2>api server...</h2>')
