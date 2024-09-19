from django.db import models

from django.db.models import Model, CharField, DateTimeField, ForeignKey, ManyToManyField, SET_NULL, IntegerField


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
    property_type = ForeignKey(HouseType, null=True, blank=True, on_delete=SET_NULL, related_name='houses_type')
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
    property = ManyToManyField(PropertyType)
    city = ForeignKey(Cities, null=True, blank=True, on_delete=SET_NULL, related_name='city')
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
    property = ForeignKey(Property, on_delete=models.CASCADE, related_name='bids')
    bidder_name = CharField(max_length=255)
    bid_amount = IntegerField(null=False)
    bid_date = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bidder_name} - {self.bid_amount} Kč"
