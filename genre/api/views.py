from rest_framework import generics, mixins, response, status
from genre.models import Genre
from genre.api.serializers import GenreSerializer

class GenrePostListView(generics.GenericAPIView, 
                          mixins.CreateModelMixin, 
                          mixins.ListModelMixin):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def get(self, request):
        data = Genre.objects.all()
        serialized_data = GenreSerializer(data,many=True).data
        return response.Response(serialized_data,status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serialized_data = GenreSerializer(data=data)
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()
            return response.Response(serialized_data.data, status=status.HTTP_201_CREATED)
    

class GenreGetUpdateDelete(generics.GenericAPIView,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def get(self, request, id):
        instance = Genre.objects.get(id=id)
        serialized_data = GenreSerializer(instance=instance).data
        return response.Response(serialized_data)
        
    def put(self, request, id):
        data = request.data
        instance = Genre.objects.get(id=id)
        serialized_data = GenreSerializer(instance=instance,data=data)
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()
            return response.Response()

    def patch(self, request, id):
        data = request.data
        instance = Genre.objects.get(id=id)
        serialized_data = GenreSerializer(instance=instance,data=data,partial=True)
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()
            return response.Response()

    def delete(self, request, id):
        instance = Genre.objects.get(id=id)
        instance.delete()
        return response.Response()