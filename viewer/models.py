from django.db import models

from django.db.models import Model, CharField, DateTimeField, ForeignKey, SET_NULL, IntegerField, ImageField, TextField, \
    ManyToManyField

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
    name = CharField(max_length=150, null=False)
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
    name = CharField(max_length=150)
    property_type = ForeignKey(GroundType, null=True, blank=True, on_delete=SET_NULL, related_name='grounds')
    property_area = IntegerField(null=False)

    class Meta:
        ordering = ['name']

    def __repr__(self):
        return f"Ground(name={self.name})"

    def __str__(self):
        return f"{self.name}"


class Apartment(Model):
    name = CharField(max_length=150, null=False)
    property_type = ForeignKey(ApartmentType, null=True, blank=True, on_delete=SET_NULL, related_name='apartments')
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

    def __str__(self):
        if self.house:
            return f"{self.house}"
        if self.ground:
            return f"{self.ground}"
        if self.apartment:
            return f"{self.apartment}"


class Auction(Model):
    property_type = ForeignKey(PropertyType, null=True, blank=True, on_delete=SET_NULL, related_name='auction')
    city = ForeignKey(Cities, null=True, blank=True, on_delete=SET_NULL, related_name='city')
    address = CharField(max_length=50, null=False)
    estimate_value = IntegerField(null=False)
    auction_assurance = IntegerField(null=False)
    min_bid = IntegerField(null=False)
    date_auction = DateTimeField(null=False)


    def loc_time(self):
        local = time.localtime()
        return f"{local[2]}.{local[1]}.{local[0]} {local[3]}:{local[4]}"


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
        time_difference = then - now
        return time_difference

    class Meta:
        verbose_name_plural = "Auctions"

    def __repr__(self):
        return f"Auction(name={self.address})"

    def __str__(self):
        return f"{self.property_type}"


class Bid(Model):
    auction = ForeignKey(Auction, null=True, blank=True, on_delete=models.CASCADE)
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


class Image(Model):
    image = ImageField(upload_to='images/', default=None, null=False, blank=False)
    house = ForeignKey(House, on_delete=SET_NULL, null=True, blank=True, related_name='images')
    apartment = ForeignKey(Apartment, on_delete=SET_NULL, null=True, blank=True, related_name='images')
    ground = ForeignKey(Ground, on_delete=SET_NULL, null=True, blank=True, related_name='images')
    auctions = ManyToManyField(Auction, blank=True, related_name='images')
    description = TextField(null=True, blank=True)

    def __repr__(self):
        return f"Image(image={self.image}, auctions={self.auctions}, description={self.description})"

    def __str__(self):
        return f"Image: {self.image}, {self.description}"