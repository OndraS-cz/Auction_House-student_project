
from django.test import TestCase

from viewer.forms import CitiesModelForm


class CreatorFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass


    def test_cities_model_form(self):
        form = CitiesModelForm(
            data={
                'name': 'Brno'
        }
        )
        print(f"\ntest_cities_is_valid: {form.data}")
        self.assertTrue(form.is_valid())
