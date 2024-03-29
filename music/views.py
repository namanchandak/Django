from django.shortcuts import render
from .models import Album
from django.http import Http404
# Create your views here.

from django.http import HttpResponse

def index(request):
    all_albums = Album.objects.all()

    return render(request, 'music/index.html',{ 'all_albums' : all_albums})

def detail(request, album_id):
    try :
        album = Album.objects.get(pk = album_id)
    except Album.DoesNotExist:
        raise Http404("Album not exist")
    return render(request, 'music/detail.html', { 'album' : album})