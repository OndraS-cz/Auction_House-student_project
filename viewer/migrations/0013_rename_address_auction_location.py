# Generated by Django 4.2.16 on 2024-09-25 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0012_alter_apartment_name_alter_ground_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auction',
            old_name='address',
            new_name='location',
        ),
    ]