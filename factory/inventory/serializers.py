import models
from rest_framework import serializers


class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Manufacturer
        fields = ('url', 'id', 'name', 'address', 'phone')


class InventoryItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.InventoryItem
        fields = ('url', 'id', 'name', 'manufacturer', 'description',
                  'size', 'weight', 'unit_of_issue', 'quantity',
                  'last_changed')