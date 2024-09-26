# Generated by Django 5.1.1 on 2024-09-23 08:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0002_alter_apartment_options_alter_apartmenttype_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='property',
        ),
        migrations.AddField(
            model_name='property',
            name='property_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='property', to='viewer.propertytype'),
        ),
    ]