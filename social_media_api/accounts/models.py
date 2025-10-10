from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class user (AbstractUser):
    bio = models.textfield(blank=True)
    profile_picture =models.Imagefield(updatte_to='profiles/',null=True, blank =True)
    followers = models.manytomanyfield('self', symmetrical=False, related_name='following', blank=True)
    def __str__(self):
        return self.username

