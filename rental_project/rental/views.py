from rest_framework import viewsets
from .models import CarRental
from .serializers import CarRentalSerializer

class CarRentalViewSet(viewsets.ModelViewSet):
    queryset = CarRental.objects.all()
    serializer_class = CarRentalSerializer