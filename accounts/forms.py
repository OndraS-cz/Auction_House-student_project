from django.contrib.auth.forms import UserCreationForm
from django.db.transaction import atomic
from django.forms import DateField, NumberInput, CharField, Textarea

from accounts.models import Profile


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2', 'nr_id_card', 'validity_id_card']

    date_of_birth = DateField(widget=NumberInput(attrs={'type': 'date'}), label="Datum narození:", required=True)
    validity_id_card = DateField(widget=NumberInput(attrs={'type': 'date'}), label="Datum platnosti OP:", required=True)

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
