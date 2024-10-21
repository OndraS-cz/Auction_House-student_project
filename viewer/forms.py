from django.forms import CharField, ModelChoiceField, IntegerField, ModelForm, Textarea, DateTimeField, ImageField, \
    Form, ChoiceField

from viewer.models import HouseType, GroundType, ApartmentType, Cities, PropertyType, House, Ground, Apartment, Auction, \
    Image, Bid


PROPERTY_TYPE_CHOICES = [
    ('house', 'Dům'),
    ('apartment', 'Byt'),
    ('ground', 'Pozemek'),
]

class PropertyTypeForm(Form):
    property_type = ChoiceField(choices=PROPERTY_TYPE_CHOICES, label="Vyberte typ nemovitosti")

class HouseForm(ModelForm):
    class Meta:
        model = House
        fields = ['name', 'house_type', 'area', 'plot_area', 'garden_area', 'description']

    name = CharField(label="Název domu", required=True)
    house_type = ModelChoiceField(queryset=HouseType.objects.all(), label="Kategorie domu", required=True)
    area = IntegerField(label="Celková plocha", required=True)
    plot_area = IntegerField(label="Zastavěná plocha", required=False)
    garden_area = IntegerField(label="Výměra pozemku", required=False)
    description = CharField(widget=Textarea, label="Popis domu", required=True)


class ApartmentForm(ModelForm):
    class Meta:
        model = Apartment
        fields = ['name', 'apartment_type', 'area', 'description']

    name = CharField(label="Název bytu", required=True)
    apartment_type = ModelChoiceField(queryset=ApartmentType.objects.all(), label="Kategorie bytu", required=True)
    area = IntegerField(label="Výměra bytu", required=True)
    description = CharField(widget=Textarea, label="Popis bytu", required=False)


class GroundForm(ModelForm):
    class Meta:
        model = Ground
        fields = ['name', 'ground_type', 'property_area', 'description']

    name = CharField(label="Název pozemku", required=True)
    ground_type = ModelChoiceField(queryset=GroundType.objects.all(), label="Kategorie pozemku", required=True)
    property_area = IntegerField(label="Výměra pozemku", required=False)
    description = CharField(widget=Textarea, label="Popis pozemku", required=False)


class HouseModelForm(ModelForm):
    class Meta:
        model = House
        fields = '__all__'

    name = CharField(label="Název nemovitosti", required=True)
    property_type = ModelChoiceField(queryset=HouseType.objects.all(), label="Kategorie domu", required=True)
    area = IntegerField(label="Celková výměra", required=False)
    plot_area = IntegerField(label="Zastavěná plocha", required=False)
    garden_area = IntegerField(label="Výměra pozemku", required=False)
    description = CharField(widget=Textarea, label="Popis nemovitosti", required=False)


class ApartmentModelForm(ModelForm):
    class Meta:
        model = Apartment
        fields = '__all__'

    name = CharField(label="Název nemovitosti", required=True)
    property_type = ModelChoiceField(queryset=ApartmentType.objects.all(), label="Kategorie bytu", required=True)
    area = IntegerField(label="Výměra bytu", required=False)
    description = CharField(widget=Textarea, label="Popis nemovitosti", required=False)


class GroundModelForm(ModelForm):
    class Meta:
        model = Ground
        fields = '__all__'

    name = CharField(label="Název nemovitosti", required=True)
    property_type = ModelChoiceField(queryset=GroundType.objects.all(), label="Kategorie pozemku", required=True)
    property_area = IntegerField(label="Výměra pozemku", required=False)
    description = CharField(widget=Textarea, label="Popis nemovitosti", required=False)


class PropertyTypeModelForm(ModelForm):
    class Meta:
        model = PropertyType
        fields = '__all__'

    house = ModelChoiceField(required=False, queryset=House.objects.all(), label="Rodinný dům")
    ground = ModelChoiceField(required=False, queryset=Ground.objects.all(), label="Pozemek")
    apartment = ModelChoiceField(required=False, queryset=Apartment.objects.all(), label="Byt")


class AuctionModelForm(ModelForm):
    class Meta:
        model = Auction
        fields = '__all__'
        exclude = ['act_value']

    property_type = ModelChoiceField(queryset=PropertyType.objects.all(), label="Nemovitost", required=True)
    city = ModelChoiceField(queryset=Cities.objects.all(), label="Okres")
    location = CharField(label="Adresa (lokace)")
    estimate_value = IntegerField(label="Odhadní cena", required=True)
    min_value = IntegerField(label="Nejnižší podání", required=True)
    auction_assurance = IntegerField(label="Výše dražební jistoty", required=True)
    min_bid = IntegerField(label="Minimální příhoz", required=True)
    date_auction = DateTimeField(label="Datum aukce")
    date_end_auction = DateTimeField(label="Datum konce aukce")
    description = CharField(widget=Textarea, label="Popis aukce")
    image = ImageField(label="Náhledový obrázek", required=False)


class ImageModelForm(ModelForm):
    class Meta:
        model = Image
        fields = '__all__'

    image = ImageField(label="Fotogalerie")
    house = ModelChoiceField(required=False, queryset=House.objects.all(), label="Vyber příslušný dům")
    apartment = ModelChoiceField(required=False,queryset=Apartment.objects.all(), label="Vyber příslušný byt")
    ground = ModelChoiceField(required=False,queryset=Ground.objects.all(), label="Vyber příslušný pozemek")
    auctions = ModelChoiceField(required=False, queryset=Auction.objects.all(), label="Vyber příslušnou aukci")
    description = CharField(widget=Textarea, label="Popis obrázku", required=False)


class BidModelForm(ModelForm):

    class Meta:
        model = Bid
        fields = ['bid_amount']


class CitiesModelForm(ModelForm):
    class Meta:
        model = Cities
        fields = '__all__'

    name = CharField(label="Nový okres")


class HouseTypeModelForm(ModelForm):
    class Meta:
        model = HouseType
        fields = '__all__'

    property_type = CharField(label="Kategorie domu")


class ApartmentTypeModelForm(ModelForm):
    class Meta:
        model = ApartmentType
        fields = '__all__'

    property_type = CharField(label="Kategorie bytu")


class GroundTypeModelForm(ModelForm):
    class Meta:
        model = GroundType
        fields = '__all__'

    property_type = CharField(label="Kategorie pozemku")
