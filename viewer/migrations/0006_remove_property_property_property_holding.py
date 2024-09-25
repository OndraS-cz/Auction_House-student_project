# Generated by Django 4.2.16 on 2024-09-20 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0005_rename_holding_property_property'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='property',
        ),
        migrations.AddField(
            model_name='property',
            name='holding',
            field=models.ManyToManyField(to='viewer.propertytype'),
        ),
    ]
