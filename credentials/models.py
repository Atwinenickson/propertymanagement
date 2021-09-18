from django.db import models
from django.contrib.auth.models import User

import datetime, time
from datetime import date, datetime, timedelta
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, Group, Permission, PermissionsMixin

class HouseType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name


# let user enter the landlord details together with the property profile, and we save the user then pick his obj to save here
class Property(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True, blank=True)
    # if no blocks, one default block(poperty item) is created
    has_blocks = models.BooleanField(default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    landlord = models.ForeignKey(User, on_delete=models.CASCADE, related_name='landlord')
    
    def __str__(self):
        return self.name

# this is the block
class PropertyItem(models.Model):
    name = models.CharField(max_length=100)
    propertyid = models.ForeignKey(Property, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, null=True, blank=True)
    # RESIDENTIAL, COMMERCIAL
    property_type = models.CharField(max_length=255, default="RESIDENTIAL")
    # BANGALO, FLAT
    structure = models.CharField(max_length=255, default="BANGALO")
    has_floors = models.BooleanField(default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class Floor(models.Model):
    name = models.CharField(max_length=100)
    propertyitem = models.ForeignKey(PropertyItem, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)


class Unit(models.Model):
    name = models.CharField(max_length=100)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    housetype = models.ForeignKey(HouseType(), on_delete=models.CASCADE)
    description = models.CharField(max_length=255, null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)