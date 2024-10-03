
from django.test import TestCase

from viewer.forms import CitiesModelForm, HouseModelForm, AuctionModelForm, HouseTypeModelForm, GroundTypeModelForm


class CreatorFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass

    def test_auction_model_form(self):
        form = AuctionModelForm(
            data={
                'location': 'Brno',
                'estimate_value': '5000000',
                'min_value': '3500000',
                'auction_assurance': '1000000',
                'min_bid': '200000',
                'date_auction': '2024-10-22',
                'date_end_auction': '2024-10-22',
                'description': 'Podrobnosti'

        }
        )
        print(f"\ntest_cities_is_valid: {form.data}")
        self.assertTrue(form.is_valid())


    def test_house_model_form(self):
        form = HouseModelForm(
            data={
                'name': 'Cihlový dům',
                'area': '89',
                'plot_area': '55',
                'garden_area': '100',
                'description': 'Popis'

        }
        )
        print(f"\ntest_cities_is_valid: {form.data}")
        self.assertTrue(form.is_valid())

    def test_cities_model_form(self):
        form = CitiesModelForm(
            data={
                'name': 'Brno'
        }
        )
        print(f"\ntest_cities_is_valid: {form.data}")
        self.assertTrue(form.is_valid())

    def test_house_type_model_form(self):
        form = HouseTypeModelForm(
            data={
                'property_type': '3+1'
        }
        )
        print(f"\ntest_cities_is_valid: {form.data}")
        self.assertTrue(form.is_valid())

    def test_ground_type_model_form(self):
        form = GroundTypeModelForm(
            data={
                'property_type': 'Les'
        }
        )
        print(f"\ntest_cities_is_valid: {form.data}")
        self.assertTrue(form.is_valid())

