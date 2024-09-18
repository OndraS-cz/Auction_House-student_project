from django.db import models

from django.db.models import Model, CharField, DateTimeField, ForeignKey, ManyToManyField, SET_NULL
from django.forms import IntegerField


class Cities(Model):
    name = CharField(max_length=20, null=False)


class HouseType(Model):
    property_type = CharField(max_length=10, null=False)


class GroundType(Model):
    property_type = CharField(max_length=30, null=False)


class ApartmentType(Model):
    property_type = CharField(max_length=30, null=False)


class House(Model):
    name = CharField(max_length=50, null=False)
    area = IntegerField(null=False, blank=False)
    property_type = ForeignKey(HouseType, null=False, blank=False, on_delete=SET_NULL)
    plot_area = IntegerField(null=False)
    garden_area = IntegerField(null=False)


class Ground(Model):
    name = CharField(max_length=50)
    property_type = ForeignKey(GroundType, null=False, blank=False, on_delete=SET_NULL)
    property_area = IntegerField(null=False)


class Apartment(Model):
    name = CharField(max_length=50, null=False)
    property_type = ForeignKey(ApartmentType, null=False, blank=False, on_delete=SET_NULL)
    area = IntegerField(null=False)


class PropertyType(Model):
    house = ForeignKey(House, null=False, blank=False, on_delete=SET_NULL)
    ground = ForeignKey(Ground, null=False, blank=False, on_delete=SET_NULL)
    apartment = ForeignKey(Apartment, null=False, blank=False, on_delete=SET_NULL)


class Property(Model):
    property = ManyToManyField(PropertyType)
    city = ForeignKey(Cities, null=False, blank=False, on_delete=SET_NULL)
    address = CharField(max_length=50, null=False)
    estimate_value = IntegerField(null=False)
    auction_assurance = IntegerField(null=False)
    min_bit = IntegerField(null=False)
    bit = IntegerField(null=False)
    date_auction = DateTimeField(null=False)


class Bid(Model):
    property = ForeignKey(Property, on_delete=models.CASCADE)
    bidder_name = CharField(max_length=255)
    bid_amount = IntegerField(max_digits=10)
    bid_date = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bidder_name} - {self.bid_amount} Kč"
