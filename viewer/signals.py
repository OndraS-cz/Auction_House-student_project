from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from django.dispatch import receiver

# Automatické přiřazování nového registrovaného uživatele do skupiny Users

@receiver(post_save, sender=User)
def add_user_to_group(sender, instance, created, **kwargs):
    if created:
        group, created = Group.objects.get_or_create(name='Users')
        instance.groups.add(group)
