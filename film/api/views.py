from django.http.response import HttpResponse
from django_filters import CharFilter
from django_filters.rest_framework import filterset
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from film.models import Film
from film.api.serializers import FilmSerializer, HelloWorldSerializer
from django_filters import FilterSet
from rest_framework import filters


#  __lte -> Less than or equal
#  __gte -> Greater than or equal
#  __lt -> Less than
#  __gt -> Greater than

class FilmFilter(FilterSet):
    production_year = CharFilter(
        field_name='production_year', method='production_year_filter')

    def production_year_filter(self, queryset, name, value):
        return queryset.filter(production_year__year=value)
        
    class Meta:
            model = Film
            fields = {
                'production_year': ('lte', 'gte'),
                'duration': ('exact','lt','gt')
            }


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.select_related('finance').prefetch_related('countries','facts').all()
    serializer_class = FilmSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter,
                       filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['production_year', 'duration','countries__id']
    search_fields = ['title', 'slogan']
    ordering_fields = ['production_year']
    # filter_class = FilmFilter # !!!!!! SWAGGER MAY NOT UPDATE UI BECAUSE OF CACHE !!!!!!

    # detail - on/off ID in request
    @action(detail=False, methods=['post'], 
    permission_classes=[permissions.AllowAny], 
    url_path='hello_world',serializer_class=HelloWorldSerializer)
    def hello_world(self, request):
        hello_serializer = HelloWorldSerializer(data=request.data)
        if hello_serializer.is_valid(raise_exception=True):
            return HttpResponse(hello_serializer.data['text'])
        

