from django.urls import path
from .views import MovieView

urlpatterns = [
    path('movie-view', MovieView.as_view(), name='movie-view')
]