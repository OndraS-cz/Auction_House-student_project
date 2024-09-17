from django.db import models

from django.db.models import Model, CharField, DateTimeField, ForeignKey
from django.forms import IntegerField


class Cities(Model):
    name = CharField(max_length=20)


class HouseType(Model):
    property_type = CharField(max_length=10)


class GroundType(Model):
    property_type = CharField(max_length=30)


class ApartmentType(Model):
    property_type = CharField(max_length=30)


class PropertyType(Model):
    property = CharField(max_length=30)


class House(Model):
    name = CharField(max_length=50)
    area = IntegerField(null=False)
    property_type = ForeignKey(HouseType)
    plot_area = IntegerField(null=False)
    garden_area = IntegerField(null=False)


class Ground(Model):
    name = CharField(max_length=50)
    property_type = ForeignKey(GroundType)
    property_area = IntegerField(null=False)


class Apartment(Model):
    name = CharField(max_length=50)
    property_type = ForeignKey(ApartmentType)
    area = IntegerField(null=False)


class Property(Model):
    property = ForeignKey(PropertyType)
    city = ForeignKey(Cities)
    address = CharField(max_length=50)
    estimate_value = IntegerField(null=False)
    auction_assurance = IntegerField(null=False)
    min_bit = IntegerField(null=False)
    bit = IntegerField(null=False)
    date_auction = DateTimeField(null=False)
