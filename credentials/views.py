from rest_framework import viewsets

from .serializers import HouseTypeSerializer, PropertySerializer, PropertyItemSerializer, FloorSerializer, UnitSerializer
from .models import HouseType, Property, PropertyItem, Floor, Unit


class HouseTypeViewSet(viewsets.ModelViewSet):
   queryset = HouseType.objects.all()
   serializer_class = HouseTypeSerializer


class PropertyViewSet(viewsets.ModelViewSet):
   queryset = Property.objects.all()
   serializer_class = PropertySerializer

class PropertyItemViewSet(viewsets.ModelViewSet):
   queryset = PropertyItem.objects.all()
   serializer_class = PropertyItemSerializer


class FloorViewSet(viewsets.ModelViewSet):
   queryset = Floor.objects.all()
   serializer_class = FloorSerializer

class UnitViewSet(viewsets.ModelViewSet):
   queryset = Unit.objects.all()
   serializer_class = UnitSerializer