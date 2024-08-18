from django.shortcuts import render
from .models import *

def index(request):
    user = request.user
    movies = user.movies.all()
    print(movies)
    return render(request, 'index.html', {
        'movies': movies
    })