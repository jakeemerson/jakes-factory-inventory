from rest_framework import viewsets
from serializers import InventoryItemSerializer, ManufacturerSerializer
from models import InventoryItem, Manufacturer


class ManufacturerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Manufacturer.objects.all().order_by('name')
    serializer_class = ManufacturerSerializer


class InventoryItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = InventoryItem.objects.all().order_by('manufacturer', 'name')
    serializer_class = InventoryItemSerializer
