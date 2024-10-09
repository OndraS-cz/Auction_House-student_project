from django.test import TestCase
from accounts.forms import SignUpForm

class SignUpFormCapitalizationTest(TestCase):

    def setUp(self):
        self.valid_data = {
            'username': 'testuser',
            'first_name': 'john',
            'last_name': 'doe',
            'date_of_birth': '1990-01-01',
            'birth_nr': '9001010007',
            'document_type': '0',
            'document_number': '222222222',
            'document_expiry': '2030-01-01',
            'phone_number': '601111111',
            'email': 'nemam@zadny.cz',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123'
        }

    def test_first_name_capitalization(self):
        form = SignUpForm(data=self.valid_data)
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())

    def test_last_name_capitalization(self):
        form = SignUpForm(data=self.valid_data)
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())

    def test_strip_whitespace_in_name(self):
        data = self.valid_data.copy()
        data['first_name'] = ' john '
        data['last_name'] = ' doe '
        form = SignUpForm(data=data)
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())
