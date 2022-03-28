from django.shortcuts import render, get_object_or_404
from .models import Movie, Director, Actor
from django.db.models import F, Sum, Min, Max, Count, Avg


# Create your views here.

def show_all_movie(request):
    movies = Movie.objects.order_by(F('year').desc(nulls_first=type), 'rating')
    movies = Movie.objects.filter(rating=83)
    # for i in movies:
    #    i.save()
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('year'), Count('id'))
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies,
        'agg': agg
    })


def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie
    })


def show_directors(request):
    directors = Director.objects.order_by('first_name')
    return render(request, 'movie_app/directors.html', {'directors': directors})


def show_id_director(request, id: int):
    director = get_object_or_404(Director, id=id)
    return render(request, 'movie_app/one_director.html', {'director': director})


def show_actors(request):
    actors = Actor.objects.all()
    return render(request, 'movie_app/actors.html', {'actors': actors})


def show_id_actor(request, id: int):
    actor = get_object_or_404(Actor, id=id)
    return render(request, 'movie_app/one_actor.html', {'actor': actor})
