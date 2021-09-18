from django.urls import include, path

from rest_framework import routers

from .views import HouseTypeViewSet, PropertyViewSet, PropertyItemViewSet, FloorViewSet, UnitViewSet

router = routers.DefaultRouter()
router.register(r'housetype', HouseTypeViewSet)
router.register(r'property', PropertyViewSet)
router.register(r'propertyitem', PropertyItemViewSet)
router.register(r'floor', FloorViewSet)
router.register(r'unit', UnitViewSet)

urlpatterns = [
   path('', include(router.urls)),
]