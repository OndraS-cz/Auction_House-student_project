# Generated by Django 4.2.15 on 2024-09-20 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='property',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='property', to='viewer.propertytype'),
        ),
    ]