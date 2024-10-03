from datetime import time

from django.test import TestCase



# Create your tests here.

class ExampleTestClass(TestCase):

    @classmethod
    def test_loc_time(self):
        self.assertEqual(1, 1)