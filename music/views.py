from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> This is music </h1>")

def detail(request, album_id):
    return HttpResponse("<h2>Details For Album id:" + str(album_id) +  "</h2>")