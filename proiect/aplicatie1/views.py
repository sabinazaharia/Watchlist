from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from aplicatie1.models import Watchlist
from aplicatie2.models import Movies

score = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10))


class WatchlistView(LoginRequiredMixin, ListView):
    model = Watchlist
    template_name = 'aplicatie1/watchlist_index.html'


class UpdateWatchlistView(LoginRequiredMixin, UpdateView):
    model = Watchlist
    fields = ['title', 'year']
    template_name = 'aplicatie1/watchlist_form.html'

    def get_success_url(self):
        return reverse('watchlist:lista_watchlist')

@login_required
def delete_watchlist(request, pk):
    # delete
    info = Watchlist.objects.get(id=pk)
    Watchlist.objects.filter(id=pk).delete()
    Movies.objects.filter(title=info.title).update(added=0)
    return redirect('watchlist:lista_watchlist')

@login_required
def watched_watchlist(request, pk):
    # mark as watched
    Watchlist.objects.filter(id=pk).update(watched=1)
    return redirect('watchlist:lista_watchlist')


@login_required
def activate_watchlist(request, pk):
    # mark as unwatched
    Watchlist.objects.filter(id=pk).update(watched=0)
    return redirect('watchlist:lista_watchlist')


class RateWatchlistView(LoginRequiredMixin, UpdateView):
    model = Watchlist
    fields = ['your_rating']
    template_name = 'aplicatie1/watchlist_rate.html'

    def get_success_url(self):
        return reverse('watchlist:lista_watchlist')
