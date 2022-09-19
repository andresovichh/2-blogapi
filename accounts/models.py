from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
"""
        The models.py file is where we define the data
        we want in our database.
"""


class CustomUser(AbstractUser):
    """ Creating a custom user class"""
    name = models.CharField(null=True, blank=True, max_length=100)
