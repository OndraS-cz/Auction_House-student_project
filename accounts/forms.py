from datetime import date

from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.db.transaction import atomic
from django.forms import DateField, NumberInput, IntegerField, CharField

from accounts.models import Profile


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'last_name', 'date_of_birth', 'nr_id_card', 'validity_id_card', 'phone_number', 'email', 'password1', 'password2']
    username = CharField(label="Uživatelské jméno")
    first_name = CharField(label="Křestní jméno")
    last_name = CharField(label="Příjmení")
    date_of_birth = DateField(widget=NumberInput(attrs={'type': 'date'}), label="Datum narození", required=True)
    nr_id_card = IntegerField(max_value=999999999, label="Číslo občanského průkazu")
    validity_id_card = DateField(widget=NumberInput(attrs={'type': 'date'}), label="Datum platnosti OP", required=True)
    phone_number = IntegerField(label="Mobilní telefon")


    @atomic
    def save(self, commit=True):
        self.instance.is_active = True
        user = super().save(commit)
        date_of_birth = self.cleaned_data['date_of_birth']
        profile = Profile(user=user,
                          date_of_birth=date_of_birth,)
        if commit:
            profile.save()
        return user


    def clean_name(self):
        cleaned_data = super().clean()
        initial = cleaned_data['name']
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
        cleaned_data = super().clean()
        date_of_birth = cleaned_data['date_of_birth']
        if date_of_birth and date_of_birth >= date.today():
            raise ValidationError('Datum narození musí být v minulosti!')
        return date_of_birth

    def clean_validity_id_card(self):
        cleaned_data = super().clean()
        validity_id_card = cleaned_data['validity_id_card']
        if validity_id_card and validity_id_card <= date.today():
            raise ValidationError('Datum platnosti občanského průkazu musí být pouze v budoucnosti!')
        return validity_id_card

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data['name']
        surname = cleaned_data['surname']
        if len(name.strip()) == 0 or len(surname.strip()) == 0:
            raise ValidationError('Je potřeba zadat jméno nebo příjmení')
        cleaned_data['name'] = name
        cleaned_data['surname'] = surname
        return cleaned_data
