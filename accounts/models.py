from django.contrib.auth.models import User
from django.db.models import Model, OneToOneField, CASCADE, DateField, TextField, IntegerField, CharField


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    date_of_birth = DateField(null=True, blank=True)
    birth_nr = CharField(max_length=10, null=True, blank=False)
    document_type = CharField(max_length=10, null=True, blank=False)
    document_number = CharField(max_length=15, null=True, blank=False)
    document_expiry = DateField(null=True, blank=False)
    phone_number = IntegerField(null=True, blank=False)
    email = TextField(null=True, blank=False)

    class Meta:
        ordering = ['user__username']

    def __repr__(self):
        return f"Profile(user={self.user})"

    def __str__(self):
        return f"{self.user}"
