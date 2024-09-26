from datetime import time

from django.test import TestCase

from viewer.views import auction


# Create your tests here.

class ExampleTestClass(TestCase):

    @classmethod
    def test_loc_time(self):
        result = auction.loc_time
        self.assertEqual(result, time.localtime())