from django.forms import ModelForm

from viewer.models import PropertyType, House, Ground, Apartment, Auction, Image


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
