from django.urls import path
from .views import MovieView

url_patterns = [
    path('movie-view', MovieView.as_view(), name='movie-view')
]