from django.shortcuts import render
from .serializers import MovieDataSerializer
from rest_framework.views import APIView
# Create your views here.


class MovieView(APIView):
    serializer_class = MovieDataSerializer

    def post(self):
        """
        post request for Movie View
        """
        pass
