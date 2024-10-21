import datetime
from datetime import date

from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.core.exceptions import ValidationError
from django.db.transaction import atomic
from django.forms import DateField, NumberInput, IntegerField, CharField, ChoiceField, PasswordInput

from django.utils.translation import gettext_lazy as _

from accounts.models import Profile
from accounts.check_document import check_document

password_validators_help_text_html = (
    "• Vaše heslo nesmí být příliš podobné vašim dalším osobním údajům.<br>"
    "• Vaše heslo musí obsahovat alespoň 8 znaků.<br>"
    "• Vaše heslo nemůže být běžně používané heslo.<br>"
    "• Vaše heslo nemůže být pouze číselné.<br>")


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'last_name', 'date_of_birth', 'birth_nr', 'document_type', 'document_number', 'document_expiry', 'phone_number', 'email', 'password1', 'password2']


    username = UsernameField(label="Uživatelské jméno",
                             help_text="Vyžadováno. 150 znaků nebo méně. Pouze písmena, číslice a znaky @/./+/-/_.",
                             error_messages={'unique': "Uživatelské jméno již existuje!"})
    first_name = CharField(label="Křestní jméno")
    last_name = CharField(label="Příjmení")
    date_of_birth = DateField(widget=NumberInput(attrs={'type': 'date'}), label="Datum narození", required=True)
    birth_nr = CharField(max_length=10, label="Rodné číslo (bez lomítka)", required=True)
    document_type = ChoiceField(choices=[('0', 'Občanský průkaz'), ('4', 'Cestovní pas')], label="Typ dokladu", required=True)
    document_number = CharField(max_length=15, label="Číslo dokladu", required=True)
    document_expiry = DateField(widget=NumberInput(attrs={'type': 'date'}), label="Datum platnosti dokladu", required=True)
    phone_number = IntegerField(label="Mobilní telefon")
    password1 = CharField(widget=PasswordInput,
                          label="Heslo",
                          required=True,
                          help_text=password_validators_help_text_html)
    password2 = CharField(widget=PasswordInput,
                          label="Potvrzení hesla",
                          required=True)
    error_messages = {
        "password_mismatch": _("Zadaná hesla nesouhlasí!"),
        "document_error": _("Doklad totožnosti byl nalezen v databázi neplatných dokladů! (viz https://aplikace.mvcr.cz/neplatne-doklady/)")
    }

    @atomic
    def save(self, commit=True):
        self.instance.is_active = True
        user = super().save(commit)
        user.set_password(self.cleaned_data['password1'])

        date_of_birth = self.cleaned_data['date_of_birth']
        birth_nr = self.cleaned_data['birth_nr']
        document_type = self.cleaned_data['document_type']
        document_number = self.cleaned_data['document_number']
        document_expiry = self.cleaned_data['document_expiry']
        phone_number = self.cleaned_data['phone_number']
        email = self.cleaned_data['email']
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

    def clean_first_name(self):
        cleaned_data = self.cleaned_data
        initial = cleaned_data['first_name']
        result = initial
        if initial is not None:
            result = initial.strip()
            if len(result):
                result = result.capitalize()
        return result

    def clean_last_name(self):
        cleaned_data = self.cleaned_data
        initial = cleaned_data['last_name']
        result = initial
        if initial is not None:
            result = initial.strip()
            if len(result):
                result = result.capitalize()
        return result

    def clean_date_of_birth(self):
        cleaned_data = self.cleaned_data
        date_of_birth = cleaned_data['date_of_birth']
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
        password1 = cleaned_data["password1"]
        password2 = cleaned_data["password2"]
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages["password_mismatch"],
                code='password_mismatch',
            )
        document_type = cleaned_data['document_type']
        document_number = cleaned_data['document_number']
        result = check_document(document_number, document_type)
        if not result:
            raise ValidationError(self.error_messages["document_error"])
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
            date_of_birth = datetime.date(year + (1900 if year >= 54 else 2000), month, day)
        except ValueError:
            raise ValidationError('Neplatné datum narození!')

        if len(birth_nr) == 10 and int(birth_nr) % 11 != 0:
            raise ValidationError('Neplatné rodné číslo!')
        else:
            result = True

        return birth_nr
