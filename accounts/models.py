from django.contrib.auth.models import User
from django.db.models import Model, OneToOneField, CASCADE, DateField, TextField, IntegerField


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    date_of_birth = DateField(null=True, blank=True)
    birth_nr = IntegerField(null=True, blank=True)
    nr_id_card = IntegerField(null=True, blank=True)
    validity_id_card = IntegerField(null=True, blank=True)
    phone_number = IntegerField(null=True, blank=True)
    email = TextField(null=True, blank=True)

    class Meta:
        ordering = ['user__username']

    def __repr__(self):
        return f"Profile(user={self.user})"

    def __str__(self):
        return f"{self.user}"
