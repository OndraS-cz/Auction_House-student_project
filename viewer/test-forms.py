from django.test import TestCase

from viewer.forms import CitiesModelForm, HouseForm, AuctionModelForm, HouseTypeModelForm, GroundTypeModelForm

from viewer.models import HouseType, Cities, PropertyType


class CreatorFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass

    def test_auction_model_form(self):
        city = Cities.objects.create(name='Brno')
        property_type = PropertyType.objects.create()


        form = AuctionModelForm(
            data={
                'location': 'Brno',
                'estimate_value': '5000000',
                'min_value': '3500000',
                'auction_assurance': '1000000',
                'act_value': '0',
                'min_bid': '200000',
                'date_auction': '2024-10-22',
                'date_end_auction': '2024-10-22',
                'description': 'Podrobnosti',
                'city': city.id,
                'property_type': property_type.id
            }
        )

        print(f"\ntest_auction_model_form: {form.data}")
        self.assertTrue(form.is_valid())

    def test_house_form_valid_data(self):
        house_type = HouseType.objects.create(property_type='Rodinný dům')

        form = HouseForm(data={
            'name': 'Cihlový dům',
            'area': 120,
            'plot_area': 300,
            'garden_area': 50,
            'description': 'Krásný cihlový dům s velkou zahradou',
            'house_type': house_type.id
        })
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
        print(f"\ntest_house_is_valid: {form.data}")
        self.assertTrue(form.is_valid())

    def test_ground_type_model_form(self):
        form = GroundTypeModelForm(
            data={
                'property_type': 'Les'
        }
        )
        print(f"\ntest_ground_type_is_valid: {form.data}")
        self.assertTrue(form.is_valid())
