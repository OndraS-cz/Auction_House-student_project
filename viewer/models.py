from django.db import models

from django.db.models import Model, CharField, DateTimeField, ForeignKey, SET_NULL, IntegerField, ImageField, TextField, \
    ManyToManyField

import time

import datetime

import pytz

from accounts.models import Profile


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
    description = TextField(null=True, blank=True)

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
    description = TextField(null=True, blank=True)

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
    description = TextField(null=True, blank=True)

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
    location = CharField(max_length=50, null=False)
    estimate_value = IntegerField(null=False)
    min_value = IntegerField(null=False)
    auction_assurance = IntegerField(null=False)
    min_bid = IntegerField(null=True, blank=False)
    date_auction = DateTimeField(null=False)
    date_end_auction = DateTimeField(null=False)
    description = TextField(null=True, blank=True)


    """def time_key(self):
        if self.date_end_auction.second < 10:
            if self.date_end_auction.minute < 10:
                if self.date_end_auction.hour < 10:
                    return f"{self.date_auction.month} {self.date_auction.day}, {self.date_auction.year} 0{self.date_end_auction.hour}:0{self.date_end_auction.minute}:0{self.date_end_auction.second}"
                return f"{self.date_auction.month} {self.date_auction.day}, {self.date_auction.year} {self.date_end_auction.hour}:0{self.date_end_auction.minute}:0{self.date_end_auction.second}"
            return f"{self.date_auction.month} {self.date_auction.day}, {self.date_auction.year} {self.date_end_auction.hour}:{self.date_end_auction.minute}:0{self.date_end_auction.second}"

        if self.date_end_auction.minute < 10:
            if self.date_end_auction.hour < 10:
                if self.date_end_auction.second < 10:
                    return f"{self.date_auction.month} {self.date_auction.day}, {self.date_auction.year} 0{self.date_end_auction.hour}:0{self.date_end_auction.minute}:0{self.date_end_auction.second}"
                return f"{self.date_auction.month} {self.date_auction.day}, {self.date_auction.year} 0{self.date_end_auction.hour}:0{self.date_end_auction.minute}:{self.date_end_auction.second}"
            return f"{self.date_auction.month} {self.date_auction.day}, {self.date_auction.year} {self.date_end_auction.hour}:0{self.date_end_auction.minute}:{self.date_end_auction.second}"

        if self.date_end_auction.hour < 10:
            if self.date_end_auction.second < 10:
                if self.date_end_auction.minute < 10:
                    return f"{self.date_auction.month} {self.date_auction.day}, {self.date_auction.year} 0{self.date_end_auction.hour}:0{self.date_end_auction.minute}:0{self.date_end_auction.second}"
                return f"{self.date_auction.month} {self.date_auction.day}, {self.date_auction.year} 0{self.date_end_auction.hour}:{self.date_end_auction.minute}:0{self.date_end_auction.second}"
            return f"{self.date_auction.month} {self.date_auction.day}, {self.date_auction.year} 0{self.date_end_auction.hour}:{self.date_end_auction.minute}:{self.date_end_auction.second}"
        else:
            return f"{self.date_auction.month} {self.date_auction.day}, {self.date_auction.year} {self.date_end_auction.hour}:{self.date_end_auction.minute}:{self.date_end_auction.second}"
"""
    def time_set(self):
        then = self.date_auction.replace(tzinfo=pytz.utc)
        now = datetime.datetime.now().replace(tzinfo=pytz.utc)
        time_diference = then - now

        if Bid.create and time_diference.total_seconds() < 300:
            self.date_end_auction = now + datetime.timedelta(minutes=5)


    def loc_time(self):
        local = time.localtime()
        return f"{local[2]}.{local[1]}.{local[0]} {local[3]}:{local[4]}"


    def time_to(self):
            then = self.date_auction.replace(tzinfo=pytz.utc)
            now = datetime.datetime.now().replace(tzinfo=pytz.utc)
            time_difference = then - now
            return time_difference


    def time_of(self):
        now = datetime.datetime.now().replace(tzinfo=pytz.utc)
        then = self.date_end_auction.replace(tzinfo=pytz.utc)
        result = then - now
        if now < then:
            return result
        else:
            return "Konec"


    def difference(self):
        now = datetime.datetime.now().replace(tzinfo=pytz.utc)
        then = self.date_end_auction.replace(tzinfo=pytz.utc)
        result = then - now
        if now < then:
            return result
        else:
            return "Konec"


    def in_progress(self):
        auction_start = self.date_auction.replace(tzinfo=pytz.utc)
        actual_time = datetime.datetime.now().replace(tzinfo=pytz.utc)
        auction_end = self.date_end_auction.replace(tzinfo=pytz.utc)
        if actual_time > auction_start and actual_time < auction_end:
            return True
        else:
            return False

    def isnot_start(self):
        auction_start = self.date_auction.replace(tzinfo=pytz.utc)
        actual_time = datetime.datetime.now().replace(tzinfo=pytz.utc)
        if actual_time < auction_start:
            return True
        else:
            return False


    def end(self):
        actual_time = datetime.datetime.now().replace(tzinfo=pytz.utc)
        auction_end = self.date_end_auction.replace(tzinfo=pytz.utc)
        if actual_time > auction_end:
            return True
        else:
            return False


    class Meta:
        verbose_name_plural = "Auctions"


    def __repr__(self):
        return f"Auction(name={self.property_type}, {self.location})"


    def __str__(self):
        return f"{self.property_type} ({self.location})"


class Bid(Model):
    auction = ForeignKey(Auction, null=True, blank=True, on_delete=models.CASCADE, related_name='bid')
    user = ForeignKey(Profile, null=True, blank=True, on_delete=SET_NULL, related_name='bid')
    bid_amount = IntegerField(null=False)
    created = DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.bidder_name} - {self.bid_amount} Kč"

    @staticmethod
    def anonymization_name(name):
        if len(name) <= 2:
            return name
        else:
            return name[0] + '*' * (len(name) - 2) + name[-1]


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
