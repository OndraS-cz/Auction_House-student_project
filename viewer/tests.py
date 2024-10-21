from datetime import time

from django.test import TestCase



# Create your tests here.

class ExampleTestClass(TestCase):

    @classmethod
    def test_add(self):
        print("Test method: test_add")
        result = 1 + 4
        self.assertEqual(result, 5)
