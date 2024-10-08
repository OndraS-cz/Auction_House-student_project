from django.db.models.fields import TextField
from django.forms import Form, CharField, ModelChoiceField, IntegerField, DateField, ModelForm, NumberInput, forms, \
    DateTimeField, ChoiceField, Textarea

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

    property_type = ModelChoiceField(queryset=PropertyType.objects.all(), label="Nemovitost:")
    city = ModelChoiceField(queryset=Cities.objects.all(), label="Město:")
    location = CharField(label="Adresa (lokace):")
    estimate_value = IntegerField(label="Odhadní cena:")
    min_value = IntegerField(label="Nejnižší podání:")
    auction_assurance = IntegerField(label="Výše dražební jistoty:")
    min_bid = IntegerField(label="Minimální příhoz:")
    date_auction = DateTimeField(label="Datum aukce:")
    date_end_auction = DateTimeField(label="Datum konce aukce:")
    description = CharField(widget=Textarea, label="Popis aukce:")


class ImageModelForm(ModelForm):
    class Meta:
        model = Image
        fields = '__all__'

class BidModelForm(ModelForm):

    class Meta:
        model = Bid
        fields = ['bid_amount']

    bid_amount = IntegerField(label="příhoz")

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