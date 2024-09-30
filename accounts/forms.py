from datetime import date

from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.db.models.expressions import result
from django.db.transaction import atomic
from django.forms import DateField, NumberInput, IntegerField, CharField, ChoiceField

from accounts.models import Profile
from accounts.check_document import check_document


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'last_name', 'date_of_birth', 'birth_nr', 'document_type', 'document_number', 'document_expiry', 'phone_number', 'email', 'password1', 'password2']
    # username = CharField(label="Uživatelské jméno")
    first_name = CharField(label="Křestní jméno")
    last_name = CharField(label="Příjmení")
    date_of_birth = DateField(widget=NumberInput(attrs={'type': 'date'}), label="Datum narození", required=True)
    birth_nr = CharField(max_length=10, label="Rodné číslo (bez lomítka)")
    document_type = ChoiceField(choices=[('0', 'Občanský průkaz'), ('4', 'Cestovní pas')], label="Typ dokladu")
    document_number = CharField(max_length=15, label="Číslo dokladu")
    document_expiry = DateField(widget=NumberInput(attrs={'type': 'date'}), label="Datum platnosti dokladu", required=True)
    phone_number = IntegerField(label="Mobilní telefon")


    @atomic
    def save(self, commit=True):
        self.instance.is_active = True
        user = super().save(commit)
        date_of_birth = self.cleaned_data['date_of_birth']
        birth_nr = self.cleaned_data['birth_nr']
        document_type = self.cleaned_data['document_type']
        document_number = self.cleaned_data['document_number']
        document_expiry = self.cleaned_data['document_expiry']
        phone_number = self.cleaned_data['phone_number']
        email = self.cleaned_data['email']
        result = check_document(document_number, document_type)
        print(result)
        profile = Profile(user=user,
                          date_of_birth=date_of_birth,
                          birth_nr=birth_nr,
                          document_type=document_type,
                          document_number=document_number,
                          document_expiry=document_expiry,
                          phone_number=phone_number,
                          email=email)
        if commit:
            profile.save()
        return user


    def clean_name(self):
        cleaned_data = self.cleaned_data
        initial = cleaned_data['first_name']
        print(f"initial name: '{initial}'")
        result = initial
        if initial is not None:
            result = initial.strip()
            print(f"result: '{result}'")
            if len(result):
                result = result.capitalize()
            print(f"result: '{result}'")
        return result


    def clean_date_of_birth(self):
        print("clean_date_of_birth")
        cleaned_data = self.cleaned_data
        print(f"cleaned_data: '{cleaned_data}'")
        date_of_birth = cleaned_data['date_of_birth']
        print(f"date_of_birth: '{date_of_birth}'")
        if date_of_birth and date_of_birth >= date.today():
            raise ValidationError('Datum narození musí být v minulosti!')
        return date_of_birth


    def clean_document_expiry(self):
        cleaned_data = self.cleaned_data
        document_expiry = cleaned_data['document_expiry']
        if document_expiry and document_expiry <= date.today():
            raise ValidationError('Datum platnosti občanského průkazu musí být pouze v budoucnosti!')
        return document_expiry


    def clean(self):
        cleaned_data = self.cleaned_data
        name = cleaned_data['first_name']
        surname = cleaned_data['last_name']
        if len(name.strip()) == 0 or len(surname.strip()) == 0:
            raise ValidationError('Je potřeba zadat jméno a příjmení')
        cleaned_data['first_name'] = name
        cleaned_data['last_name'] = surname
        return cleaned_data


    def clean_birth_nr(self):
        cleaned_data = self.cleaned_data
        birth_nr = cleaned_data['birth_nr']
        if len(birth_nr) != 9 and len(birth_nr) != 10:
            raise ValidationError('Neplatná délka rodného čísla!')

        year = int(birth_nr[:2])
        month = int(birth_nr[2:4])
        day = int(birth_nr[4:6])

        if month > 50:
            month -= 50

        try:
            import datetime
            date_of_birth = datetime.date(year + (1900 if year >= 54 else 2000), month, day)
        except ValueError:
            raise ValidationError('Neplatné datum narození!')

        if len(birth_nr) == 10 and int(birth_nr) % 11 != 0:
            raise ValidationError('Neplatné rodné číslo!')
        else:
            result = True

        return result, f"Rodné číslo je platné. Datum narození: {date_of_birth}"
