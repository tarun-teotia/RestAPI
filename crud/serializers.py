from rest_framework import serializers
from .models import Item, Item2

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'