from django.db import models
from django.contrib.auth.models import AbstractUser
from shortuuid.django_fields import ShortUUIDField
# Create your models here.

class User(AbstractUser):
    user_id = ShortUUIDField(unique=True,length=10, max_length=20,prefix="user-",alphabet="abcdefghijklmnopqrstuvwxyz1234567890")
    email = models.EmailField(unique=True, null=False,max_length=50)
    username = models.CharField(max_length=50)
    phone = models.CharField(max_length=25, unique=True, null=True, blank=True)
    userrole = models.CharField(max_length=50, null=False, default="user")

    

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username