from django.forms import CharField, ModelChoiceField, IntegerField, ModelForm, DateTimeField, Textarea, ImageField

from viewer.models import HouseType, GroundType, ApartmentType, Cities, PropertyType, House, Ground, Apartment, Auction, \
    Image, Bid


class HouseModelForm(ModelForm):
    class Meta:
        model = House
        fields = '__all__'

    name = CharField(label="Název nemovitosti")
    property_type = ModelChoiceField(queryset=HouseType.objects.all(), label="Počet pokojů")
    area = IntegerField(label="Celková výměra")
    plot_area = IntegerField(label="Zastavěná plocha")
    garden_area = IntegerField(label="Výměra pozemku")
    description = CharField(widget=Textarea, label="Popis nemovitosti")

class ApartmentModelForm(ModelForm):
    class Meta:
        model = Apartment
        fields = '__all__'

    name = CharField(label="Název nemovitosti")
    property_type = ModelChoiceField(queryset=ApartmentType.objects.all(), label="Kategorizace bytu")
    area = IntegerField(label="Výměra bytu")
    description = CharField(widget=Textarea, label="Popis nemovitosti")


class GroundModelForm(ModelForm):
    class Meta:
        model = Ground
        fields = '__all__'

    name = CharField(label="Název nemovitosti")
    property_type = ModelChoiceField(queryset=GroundType.objects.all(), label="Typ pozemku")
    property_area = IntegerField(label="Výměra pozemku")
    description = CharField(widget=Textarea, label="Popis nemovitosti")


class PropertyTypeModelForm(ModelForm):
    class Meta:
        model = PropertyType
        fields = '__all__'

    house = ModelChoiceField(queryset=House.objects.all(), label="Rodinný dům")
    ground = ModelChoiceField(queryset=Ground.objects.all(), label="Pozemek")
    apartment = ModelChoiceField(queryset=Apartment.objects.all(), label="Byt")


class AuctionModelForm(ModelForm):
    class Meta:
        model = Auction
        fields = '__all__'

    property_type = ModelChoiceField(queryset=PropertyType.objects.all(), label="Nemovitost")
    city = ModelChoiceField(queryset=Cities.objects.all(), label="Město")
    location = CharField(label="Adresa (lokace)")
    estimate_value = IntegerField(label="Odhadní cena")
    min_value = IntegerField(label="Nejnižší podání")
    auction_assurance = IntegerField(label="Výše dražební jistoty")
    min_bid = IntegerField(label="Minimální příhoz")
    date_auction = DateTimeField(label="Datum aukce")
    date_end_auction = DateTimeField(label="Datum konce aukce")
    description = CharField(widget=Textarea, label="Popis aukce")


class ImageModelForm(ModelForm):
    class Meta:
        model = Image
        fields = '__all__'

    image = ImageField(label="Obrázek")
    house = ModelChoiceField(queryset=HouseType.objects.all(), label="Vyber příslušný dům")
    apartment = ModelChoiceField(queryset=ApartmentType.objects.all(), label="Vyber příslušný byt")
    ground = ModelChoiceField(queryset=GroundType.objects.all(), label="Vyber příslušný pozemek")
    auctions = ModelChoiceField(queryset=Auction.objects.all(), label="Vyber příslušnou aukci")
    description = CharField(widget=Textarea, label="Popis obrázku")


class BidModelForm(ModelForm):

    class Meta:
        model = Bid
        fields = ['bid_amount']

    bid_amount = IntegerField(label="Hodnota příhozu")

class CitiesModelForm(ModelForm):
    class Meta:
        model = Cities
        fields = '__all__'

    name = CharField(label="Název města")

class HouseTypeModelForm(ModelForm):
    class Meta:
        model = HouseType
        fields = '__all__'

    property_type = CharField(label="Počet pokojů")


class ApartmentTypeModelForm(ModelForm):
    class Meta:
        model = ApartmentType
        fields = '__all__'

    property_type = CharField(label="Kategorizace bytu")


class GroundTypeModelForm(ModelForm):
    class Meta:
        model = GroundType
        fields = '__all__'

    property_type = CharField(label="Typ pozemku")
