from rest_framework import generics, mixins, response, status
from country.models import Country
from country.api.serializers import CountrySerializer

class CountryPostListView(generics.GenericAPIView, 
                          mixins.CreateModelMixin, 
                          mixins.ListModelMixin):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def get(self, request):
        data = Country.objects.all()
        serialized_data = CountrySerializer(data,many=True).data
        return response.Response(serialized_data,status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serialized_data = CountrySerializer(data=data)
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()
            return response.Response(serialized_data.data, status=status.HTTP_201_CREATED)