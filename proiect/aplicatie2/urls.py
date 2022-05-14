from django.urls import path

from aplicatie2 import views

app_name = 'movies'

urlpatterns = [
    path('', views.MoviesView.as_view(), name='lista_movies'),
    path('<int:pk>/adauga/', views.add_movie_view, name='adauga'),
    path('search/', views.search, name='cauta'),
]