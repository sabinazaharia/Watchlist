from django.urls import path

from aplicatie1 import views

app_name = 'watchlist'

urlpatterns = [
    path('', views.WatchlistView.as_view(), name='lista_watchlist'),
    path('<int:pk>/sterge/', views.delete_watchlist, name='sterge'),
    path('<int:pk>/update/', views.UpdateWatchlistView.as_view(), name='modifica'),
    path('<int:pk>/vazut/', views.watched_watchlist, name='vazut'),
    path('<int:pk>/activeaza/', views.activate_watchlist, name='activeaza'),
    path('<int:pk>/rate/', views.RateWatchlistView.as_view(), name='rate'),
]