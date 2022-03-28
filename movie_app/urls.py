from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie-detail'),
    path('directors', views.show_directors),
    path('directors/<int:id>', views.show_id_director, name='info-director'),
    path('actors', views.show_actors),
    path('actors/<int:id>', views.show_id_actor, name='info-actors'),
]
