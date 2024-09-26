# Generated by Django 5.1.1 on 2024-09-25 10:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('birth_nr', models.IntegerField(blank=True, null=True)),
                ('nr_id_card', models.IntegerField(blank=True, null=True)),
                ('validity_id_card', models.IntegerField(blank=True, null=True)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('email', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user__username'],
            },
        ),
    ]