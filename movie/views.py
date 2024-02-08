from django.shortcuts import render
from .models import Movie, Genre

# Create your views here.

def movies(request):
    title = 'movies'
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    action_movies = Movie.objects.filter(genres__name='action')
    return render(request, "movies.html", {'title': title, 'movies': movies, 'genres': genres, 'action_movies': action_movies})


def top_movies(request):
    title = 'Top Movies'
    return render(request, "top-movies.html", {'title': title})


def movie_details(request, id):
    title = 'Details'
    movie = Movie.objects.get(id = id)
    return render(request, 'movie-details.html', {'title': title, 'movie': movie})