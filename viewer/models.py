from django.db import models

from django.db.models import Model, CharField, DateTimeField, ForeignKey, ManyToManyField, SET_NULL, IntegerField


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
    property_type = ForeignKey(HouseType, null=True, blank=True, on_delete=SET_NULL, related_name='houses_type')
    plot_area = IntegerField(null=False)
    garden_area = IntegerField(null=False)


class Ground(Model):
    name = CharField(max_length=50)
    property_type = ForeignKey(GroundType, null=True, blank=True, on_delete=SET_NULL, related_name='grounds_type')
    property_area = IntegerField(null=False)


class Apartment(Model):
    name = CharField(max_length=50, null=False)
    property_type = ForeignKey(ApartmentType, null=True, blank=True, on_delete=SET_NULL, related_name='apartments_type')
    area = IntegerField(null=False)


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

    def loc_time(self):
        local = time.localtime()
        return f"{local[2]}.{local[1]}.{local[0]} {local[3]}:{local[4]}"

    def time_to(self):
        #date_auction = "10-20-2024 15:30"
        year = self.date_auction[6:10]
        month = self.date_auction[0:2]
        day = self.date_auction[3:5]
        hour = self.date_auction[11:13]
        minute = self.date_auction[14:16]
        #subjects = [month, day, hour, minute]
        #print(year, month, day, hour, minute)
        then = datetime(int(year), int(month), int(day), int(hour), int(minute))
        now = datetime.now()
        time_diference = then - now

        return time_diference


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
