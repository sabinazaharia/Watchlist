from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView

from aplicatie1.models import Watchlist
from aplicatie2.models import Movies


class MoviesView(LoginRequiredMixin, ListView):
    model = Movies
    movies_list = Movies.objects.all()
    template_name = 'aplicatie2/movies_index.html'


@login_required
def add_movie_view(request, pk):
    movie_info = Movies.objects.get(id=pk)
    Watchlist.objects.create(title=movie_info.title, year=movie_info.year, rating=movie_info.rating)
    Movies.objects.filter(id=pk).update(added=1)

    return redirect('movies:lista_movies')


@login_required
def search(request):
    results = []
    if request.method == "GET":
        query = request.GET.get('search')
        if query == '':
            query = 'None'
        results = Movies.objects.filter(Q(title=query))

    return render(request, 'aplicatie2/search.html', {'query': query, 'results': results})
