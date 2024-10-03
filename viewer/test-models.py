import datetime

from django.test import TestCase

from viewer.models import House, HouseType, PropertyType, Auction, Cities


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
        house.property_type.add(house_type)

        property = PropertyType.objects.create()
        property.house.add(house)

        auction = Auction.objects.create(
            location = "Brno",
            estimate_value = "5000000",
            auction_assurance = "3500000",
            min_bid = "200000",
            date_auction = datetime.date(2024, 10, 5),
            date_end_auction = datetime.date(2024, 11, 1),

        )


        city = Cities.objects.create(name='San Francisco')
        auction.city.add(city)


    def test_home_str(self):
        house = House.objects.get(id=1)
        self.assertEqual(house.__str__(), 'Cihlový dům')