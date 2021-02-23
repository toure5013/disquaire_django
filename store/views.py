# from django.shortcuts import render
from django.http import HttpResponse
from .models import ALBUMS


def index(request):
    message = "BISMILAHI RAHMANI RAHIM"
    message2 = "ALAHOUMA SOLI ALA MOUHAMADIN WA ALA ALIHI WA SALIM"
    return HttpResponse(message + "\n" + message2)



def listing(request):
    albums = ["<li>{}</li>".format(album['name']) for album in ALBUMS] 
    message = """<ul>{}</ul>""".format("\n".join(albums)) 
    return HttpResponse(message)


def search_album_form(request):
    form = """<form method="GET" action="">
    Search : <input type="text" name="album_name" plaholder="Enter the album name">
    </form> """
    print("request")
    print(request)
    return HttpResponse(form)


def detail(request, album_id):
    print(album_id)
    id = (int(album_id))
    print(type(id))
    album = ALBUMS[id]
    print(album)
    artists = " ".join([artist['name'] for artist in album['artists']]) 
    message = "Le nom de l'album est {}. Il a été écrit par {}".format(album['name'], artists)
    return HttpResponse(message)
