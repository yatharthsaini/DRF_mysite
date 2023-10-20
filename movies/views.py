from movies.serializers import MovieDataSerializer
from rest_framework.views import APIView
from movies.models import MovieData
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class MovieView(APIView):
    serializer_class = MovieDataSerializer
    queryset = MovieData.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response({'Message': 'Serializer is not valid'}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({'Content': 'OK'}, status=status.HTTP_200_OK)



