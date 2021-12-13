from django.http.response import Http404
from rest_framework import status, mixins, generics
from rest_framework.response import Response
from film.models import Film
from film.api.serializers import FilmSerializer

class FilmCreateListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def get(self, request):
        data = Film.objects.all()
        serialized_data = FilmSerializer(data, many=True).data
        return Response(serialized_data)

    def post(self,request):
        serialized_data = FilmSerializer(data=request.data)
        if serialized_data.is_valid(): # raise_exception=True
            serialized_data.save()
            return Response(serialized_data.data,status=status.HTTP_201_CREATED)
        else:
            return Response('Invalid data',status=status.HTTP_400_BAD_REQUEST)

class FilmUpdateDeleteView(mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      generics.GenericAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def get_object(self, id):
        try:
            return Film.objects.get(id=id)
        except Film.DoesNotExist:
            raise Http404

    def get(self, request, id):
        wish_msg = self.get_object(id)
        serializer = FilmSerializer(wish_msg)
        return Response(serializer.data)

    def put(self, request, id):
        wish_msg = self.get_object(id)
        serializer = FilmSerializer(wish_msg, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        wish_msg = self.get_object(id)
        serializer = FilmSerializer(
            wish_msg, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        wish_msg = self.get_object(id)
        wish_msg.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





# class FilmCreateListView(mixins.ListModelMixin,
#                                 mixins.CreateModelMixin,
#                                 generics.GenericAPIView):
#     queryset = Film.objects.all()
#     serializer_class = FilmSerializer

#     def get(self, request):
#         serializer = FilmSerializer(Film.objects.all(), many=True)
#         return Response(serializer.data)

#     def post(self, request):  # post
#         serializer = self.get_serializer(data=request.data,context={'request_method': request.method})
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
