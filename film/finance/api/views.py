from rest_framework import viewsets, permissions
from rest_framework.decorators import permission_classes
from film.finance.models import Finance
from film.finance.api.serializers import FinanceSerializer

class FinanceViewSet(viewsets.ModelViewSet):
    queryset = Finance.objects.all()
    serializer_class = FinanceSerializer
    permission_classes = [permissions.AllowAny]