from django.contrib import admin

from viewer.models import Cities, HouseType, GroundType, ApartmentType, House, Ground, Apartment, PropertyType, Auction

admin.site.register(Cities)
admin.site.register(HouseType)
admin.site.register(GroundType)
admin.site.register(ApartmentType)
admin.site.register(House)
admin.site.register(Ground)
admin.site.register(Apartment)
admin.site.register(PropertyType)
admin.site.register(Auction)

