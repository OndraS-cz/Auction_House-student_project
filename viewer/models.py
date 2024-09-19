from django.db import models

from django.db.models import Model, CharField, DateTimeField, ForeignKey, ManyToManyField, SET_NULL
from django.forms import IntegerField


class Cities(Model):
    name = CharField(max_length=20, null=False)

    class Meta:
        verbose_name_plural = "Cities"
        ordering = ['name']

    def __repr__(self):
        return f"City(name={self.name})"

    def __str__(self):
        return f"{self.name}"


class HouseType(Model):
    property_type = CharField(max_length=10, null=False)

    class Meta:
        ordering = ['property_type']

    def __repr__(self):
        return f"HouseType(name={self.property_type})"

    def __str__(self):
        return f"{self.property_type}"


class GroundType(Model):
    property_type = CharField(max_length=30, null=False)

    class Meta:
        ordering = ['property_type']

    def __repr__(self):
        return f"GroundType(name={self.property_type})"

    def __str__(self):
        return f"{self.property_type}"


class ApartmentType(Model):
    property_type = CharField(max_length=30, null=False)

    class Meta:
        ordering = ['property_type']

    def __repr__(self):
        return f"ApartmentType(name={self.property_type})"

    def __str__(self):
        return f"{self.property_type}"


class House(Model):
    name = CharField(max_length=50, null=False)
    area = IntegerField(null=False, blank=False)
    property_type = ForeignKey(HouseType, null=False, blank=False, on_delete=SET_NULL)
    plot_area = IntegerField(null=False)
    garden_area = IntegerField(null=False)

    class Meta:
        ordering = ['name']

    def __repr__(self):
        return f"House(name={self.name})"

    def __str__(self):
        return f"{self.name}"


class Ground(Model):
    name = CharField(max_length=50)
    property_type = ForeignKey(GroundType, null=False, blank=False, on_delete=SET_NULL)
    property_area = IntegerField(null=False)

    class Meta:
        ordering = ['name']

    def __repr__(self):
        return f"Ground(name={self.name})"

    def __str__(self):
        return f"{self.name}"


class Apartment(Model):
    name = CharField(max_length=50, null=False)
    property_type = ForeignKey(ApartmentType, null=False, blank=False, on_delete=SET_NULL)
    area = IntegerField(null=False)

    class Meta:
        ordering = ['name']

    def __repr__(self):
        return f"Apartment(name={self.name})"

    def __str__(self):
        return f"{self.name}"


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

    class Meta:
        verbose_name_plural = "Properties"

    def __repr__(self):
        return f"Property(name={self.property})"

    def __str__(self):
        return f"{self.property}"


class Bid(Model):
    property = ForeignKey(Property, on_delete=models.CASCADE)
    bidder_name = CharField(max_length=255)
    bid_amount = IntegerField(max_digits=10)
    bid_date = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bidder_name} - {self.bid_amount} Kč"

