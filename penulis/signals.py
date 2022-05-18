from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group

from .models import Penulis

def penulis_profile(sender, instance, created, **kwagrs):
    if created:
        group = Group.objects.get(name='penulis')
        instance.groups.add(group)
        Penulis.objects.create(
            user=instance,
            nama=instance.username,
            email=instance.email,
        )

post_save.connect(penulis_profile, sender=User)
