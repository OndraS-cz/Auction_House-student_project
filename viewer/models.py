from django.db import models

from django.db.models import Model, CharField, DateTimeField, ForeignKey
from django.forms import IntegerField


class Mesta(Model):
    název = CharField(max_length=20)

# Create your models here.
class Typ_domu(Model):
    typ_domu = CharField(max_length=10)


class Typ_nemovitosti(Model):
    typ_nemovitosti = CharField(max_length=30)




class Dum(Model):
    jmeno = CharField(max_length=50)
    rozloha = CharField(max_length=50)
    rozloha_parcely = IntegerField(null=False)
    rozloha_zahrady = IntegerField(null=False)


class Pozemek(Model):
    jmeno = CharField(max_length=50)
    typ_pozemku = CharField(max_length=50)
    rozloha_pozemku = IntegerField(null=False)

class Byt(Model):
    jmeno = CharField(max_length=50)
    typ = ForeignKey(Typ_domu)
    rozloha = CharField(max_length=50)






class Nemovitost(Model):
    nemovitost = ForeignKey(Typ_nemovitosti)
    mesto = ForeignKey(Mesta)
    adresa = CharField(max_length=50)
    odhadovana_hodnota = IntegerField(null=False)
    drazebni_jistota = IntegerField(null=False)
    min_prihoz = IntegerField(null=False)
    podání = IntegerField(null=False)
    datum_drazby = DateTimeField(null=False)
