from rest_framework import serializers

from .models import HouseType, Property, PropertyItem, Floor, Unit

class HouseTypeSerializer(serializers.ModelSerializer):
   class Meta:
       model = HouseType
       fields = '__all__'


class PropertySerializer(serializers.ModelSerializer):
   class Meta:
       model = Property
       fields = '__all__'

class PropertyItemSerializer(serializers.ModelSerializer):
   class Meta:
       model = PropertyItem
       fields = '__all__'


class FloorSerializer(serializers.ModelSerializer):
   class Meta:
       model = Floor
       fields = '__all__'

class UnitSerializer(serializers.ModelSerializer):
   class Meta:
       model = Unit
       fields = '__all__'