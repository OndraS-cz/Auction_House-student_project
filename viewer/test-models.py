from django.test import TestCase

from viewer.models import House


class AuctionModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        house1 = House.objects.create(
            name = 'Cihlový dům',
            area = '200',
            plot_area = '48',
            garden_area = '100',

        )

    def test_home_str(self):
        house = House.objects.get(id=1)
        self.assertEqual(house.__str__(), 'Cihlový dům')