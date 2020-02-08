from django.shortcuts import render, redirect
from django.http import HttpResponse
from inventory.models import *
from .forms import AlbumForm, ArtistForm
from django.contrib.auth.decorators import login_required

def index(request):
    artists = Artist.objects.all()
    return render(request, "inventory/index.html", locals())

def album_new(request):
    if request.method == "POST":
        form = AlbumForm(request.POST) 
        if form.is_valid():
            album = form.save(commit=False)
            album.save()
            return redirect('index')
    else:
        form = AlbumForm()
        return render(request, 'inventory/album_form.html', {'form': form})

def artist_new(request):
    if request.method == "POST":
        form = ArtistForm(request.POST) 
        if form.is_valid():
            artist = form.save(commit=False)
            artist.save()
            return redirect('index')
    else:
        form = ArtistForm()
        return render(request, 'inventory/artist_form.html', {'form': form})

def album_delete(request, id):
    album = Album.objects.get(id)
    if request.method == "Delete":
        album.delete()
        return redirect('index')