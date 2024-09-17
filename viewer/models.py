from django.db import models

from django.db.models import Model, CharField, DateTimeField, ForeignKey
from django.forms import IntegerField


class Cities(Model):
    name = CharField(max_length=20)

# Create your models here.
class House_type(Model):
    property_type = CharField(max_length=10)

class Ground_type(Model):
    property_type = CharField(max_length=30)

class Apartment_type(Model):
    property_type = CharField(max_length=30)


class Property_type(Model):
    property =





class House(Model):
    name = CharField(max_length=50)
    area = IntegerField(null=False)
    property_type = ForeignKey(House_type)
    plot_area = IntegerField(null=False)
    garden_area = IntegerField(null=False)


class Holding(Model):
    name = CharField(max_length=50)
    property_type = ForeignKey(Ground_type)
    property_area = IntegerField(null=False)

class Apartment(Model):
    name = CharField(max_length=50)
    property_type = ForeignKey(Apartment_type)
    area = IntegerField(null=False)







class property(Model):
    property = ForeignKey(Typ_nemovitosti)
    city = ForeignKey(Cities)
    address = CharField(max_length=50)
    estimate_value = IntegerField(null=False)
    auction_assurance = IntegerField(null=False)
    min_bit = IntegerField(null=False)
    bit = IntegerField(null=False)
    date_auction = DateTimeField(null=False)
