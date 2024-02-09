import os
import json
from django.shortcuts import render, get_object_or_404
from .models import Movie, Genre

def movies(request):
    title = 'movies'
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    
    json_file_path = os.path.join(os.path.dirname(__file__), '..', 'cleaned_data2.json')
    with open(json_file_path) as f:
        data = json.load(f)[:149]
    
    return render(request, "movies.html", {'title': title, 'movies': movies, 'genres': genres, 'data': data})


def top_movies(request):
    title = 'Top Movies'
    return render(request, "top-movies.html", {'title': title})


def movie_details(request, id):
    title = 'Details'
    
    # movie = get_object_or_404(Movie, id=id)
    
    # movie.views += 1
    # movie.save()
    
    
     # Fetching movie details from JSON file
    json_file_path = os.path.join(os.path.dirname(__file__), '..', 'cleaned_data2.json')
    with open(json_file_path) as f:
        data = json.load(f)
        # Finding the movie details in the JSON data based on its ID
        movie_data = next((m for m in data if m['id'] == id), None)

    # movie = Movie.objects.get(id = id)
    return render(request, 'movie-details.html', {'title': title, 'movie_data': movie_data,})