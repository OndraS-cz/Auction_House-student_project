import datetime

from django.test import TestCase

from viewer.models import House, HouseType, Auction


class AuctionModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        house = House.objects.create(
            name = 'Cihlový dům',
            area = '200',
            plot_area = '48',
            garden_area = '100',

        )

        house_type = HouseType.objects.create(property_type = "3+1")

        auction = Auction.objects.create(
            location = "Brno",
            estimate_value = "5000000",
            min_value = '3500000',
            auction_assurance = "3500000",
            min_bid = "200000",
            date_auction = datetime.date(2024, 10, 5),
            date_end_auction = datetime.date(2024, 11, 1),
            description = 'Podrobný popis'
        )

    def test_house_str(self):
        house = House.objects.get(id=1)
        self.assertEqual(house.__str__(), 'Cihlový dům')
        print("Test house str pass")

    def test_house_repr(self):
        house = House.objects.get(id=1)
        self.assertEqual(house.__repr__(), 'House(name=Cihlový dům)')
        print("Test house repr pass")

    def test_house_type_str(self):
        house_type = HouseType.objects.get(id=1)
        self.assertEqual(house_type.__str__(), '3+1')
        print("Test house type str pass")

    def test_house_type_repr(self):
        house_type = HouseType.objects.get(id=1)
        self.assertEqual(house_type.__repr__(), 'HouseType(name=3+1)')
        print("Test house type repr pass")

    def test_number_of_auctions_(self):
        auction = Auction.objects.get(id=1)
        auctions = Auction.objects.all()
        number_of_auctions = auctions.count()
        self.assertEqual(number_of_auctions, 1)
        print("Test number of auctions pass")
