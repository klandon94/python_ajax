from django.shortcuts import render,redirect, HttpResponse
import requests

def index(req):
    return render(req, 'itunes/index.html')

def getmovie(req):
    artist = req.POST['user_input'].replace(' ', '')
    url = "https://itunes.apple.com/search?term=" + artist + "&entity=musicVideo"

    response = requests.get(url).content

    return HttpResponse(response, content_type='application/json')
