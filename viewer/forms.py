from datetime import date
from django.contrib.admin.widgets import AdminDateWidget
from django.core.exceptions import ValidationError
from django.forms import Form, CharField, ModelChoiceField, IntegerField, DateField, ModelForm, NumberInput, forms, \
    SplitDateTimeWidget

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


class DateTimePickerInput:
    pass


class AuctionModelForm(ModelForm):
    class Meta:
        model = Auction
        fields = '__all__'

    #date_auction = DateField(required=False, widget=NumberInput(attrs={'type': 'time'}))

class ImageModelForm(ModelForm):
    class Meta:
        model = Image
        fields = '__all__'


class BidModelForm(ModelForm):

    class Meta:
        model = Bid
        fields = ['bid_amount']

    def clean(self):
        bid_amount = self.cleaned_data['bid_amount']
        auction = self.cleaned_data.get('auction')

        if auction and bid_amount < auction.min_bid:
             raise forms.ValidationError(f"Bid must be at least {auction.min_bid}")
        return bid_amount

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