from django.db import models

from django.db.models import Model, CharField, DateTimeField, ForeignKey, ManyToManyField, SET_NULL, IntegerField

import time

import datetime

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
    property_type = CharField(max_length=15, null=False)

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
    area = IntegerField(null=True, blank=True)
    property_type = ForeignKey(HouseType, null=True, blank=True, on_delete=SET_NULL, related_name='houses')
    plot_area = IntegerField(null=True, blank=True)
    garden_area = IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __repr__(self):
        return f"House(name={self.name})"

    def __str__(self):
        return f"{self.name}"


class Ground(Model):
    name = CharField(max_length=50)
    property_type = ForeignKey(GroundType, null=True, blank=True, on_delete=SET_NULL, related_name='grounds_type')
    property_area = IntegerField(null=False)

    class Meta:
        ordering = ['name']

    def __repr__(self):
        return f"Ground(name={self.name})"

    def __str__(self):
        return f"{self.name}"


class Apartment(Model):
    name = CharField(max_length=50, null=False)
    property_type = ForeignKey(ApartmentType, null=True, blank=True, on_delete=SET_NULL, related_name='apartments_type')
    area = IntegerField(null=False)

    class Meta:
        ordering = ['name']

    def __repr__(self):
        return f"Apartment(name={self.name})"

    def __str__(self):
        return f"{self.name}"


class PropertyType(Model):
    house = ForeignKey(House, null=True, blank=True, on_delete=SET_NULL, related_name='house')
    ground = ForeignKey(Ground, null=True, blank=True, on_delete=SET_NULL, related_name='ground')
    apartment = ForeignKey(Apartment, null=True, blank=True, on_delete=SET_NULL, related_name='apartment')


class Property(Model):
    property_type = ForeignKey(PropertyType, null=True, blank=True, on_delete=SET_NULL, related_name='property')
    city = ForeignKey(Cities, null=True, blank=True, on_delete=SET_NULL, related_name='city')
    address = CharField(max_length=50, null=False)
    estimate_value = IntegerField(null=False)
    auction_assurance = IntegerField(null=False)
    min_bit = IntegerField(null=False)
    bit = IntegerField(null=False)
    date_auction = DateTimeField(null=False)

    def __str__(self):
        return self.address

    def loc_time(self):
        local = time.localtime()
        return f"{local[2]}.{local[1]}.{local[0]} {local[3]}:{local[4]}"
    class Meta:
        verbose_name_plural = "Properties"

    def time_to(self):
        #date_auction = "10-20-2024 15:30"
        year = self.date_auction.year
        month = self.date_auction.month
        day = self.date_auction.day
        hour = self.date_auction.hour
        minute = self.date_auction.minute
        #subjects = [month, day, hour, minute]
        #print(year, month, day, hour, minute)
        then = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute))
        now = datetime.datetime.now()
        time_diference = then - now
    def __repr__(self):
        return f"Property(name={self.property})"

    def __str__(self):
        return f"{self.property}"


class Bid(Model):
    property = ForeignKey(Property, on_delete=models.CASCADE, related_name='bids')
    bidder_name = CharField(max_length=255)
    bid_amount = IntegerField(null=False)
    bid_date = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bidder_name} - {self.bid_amount} Kč"

    def anonymizovat_jmeno(self):
        if len(self.bidder_name) <= 2:
            return self.bidder_name  # pokud je nickname příliš krátký, vrať ho celý
        else:
            return self.bidder_name[0] + '*' * (len(self.bidder_name) - 2) + self.bidder_name[-1]
