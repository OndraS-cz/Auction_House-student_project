from django.forms import Form, CharField, ModelChoiceField, IntegerField, DateField, ModelForm, NumberInput, forms

from viewer.models import HouseType, GroundType, ApartmentType, Cities, PropertyType, House, Ground, Apartment, Auction, \
    Image, Bid


class HouseModelForm(ModelForm):
    class Meta:
        model = House
        fields = '__all__'


class ApartmentModelForm(ModelForm):
    class Meta:
        model = Apartment
        fields = '__all__'


class GroundModelForm(ModelForm):
    class Meta:
        model = Ground
        fields = '__all__'


class PropertyTypeModelForm(ModelForm):
    class Meta:
        model = PropertyType
        fields = '__all__'


class AuctionModelForm(ModelForm):
    class Meta:
        model = Auction
        fields = '__all__'


class ImageModelForm(ModelForm):
    class Meta:
        model = Image
        fields = '__all__'


class BidModelForm(ModelForm):

    class Meta:
        model = Bid
        fields = ['bid_amount']

    bid_amount = IntegerField(min_value=200000, label="příhoz")

class CitiesModelForm(ModelForm):
    class Meta:
        model = Cities
        fields = '__all__'

class HouseTypeModelForm(ModelForm):
    class Meta:
        model = HouseType
        fields = '__all__'

class ApartmentTypeModelForm(ModelForm):
    class Meta:
        model = ApartmentType
        fields = '__all__'

class GroundTypeModelForm(ModelForm):
    class Meta:
        model = GroundType
        fields = '__all__'