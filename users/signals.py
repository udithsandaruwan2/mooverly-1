from .models import Profile, StaffCode
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from .utils import local

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile, StaffCode

@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        staff_code = getattr(local, 'staff_code', None)
        profile = Profile.objects.create(
            user=user, 
            username=user.username, 
            email=user.email,
            name=user.first_name, 
            staff_code=staff_code,
        )
        
        if staff_code:
            staff_code.owner = profile
            staff_code.save()


def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()

def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()

post_save.connect(createProfile, sender=User)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)