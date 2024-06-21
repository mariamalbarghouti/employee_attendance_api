from rest_framework import serializers
from base.models import Item, ImageModel, ImageComparisonModel


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = '__all__'



class ImageComparisonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageComparisonModel
        fields = '__all__'