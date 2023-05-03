from django.db.models.signals import post_save #will be fired when the user is created and updated..
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

#craeted or upladng the user profile pic from the website.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

#saving the profile picture loaded from the website and creating the profile picture..
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()