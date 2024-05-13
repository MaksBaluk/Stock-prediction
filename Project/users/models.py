from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager


# Create your models here.


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)
    birth_year = models.PositiveSmallIntegerField(blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    # def get_username(self):
    #     if self.first_name and self.last_name:
    #         return self.first_name +' '+ self.last_name
    #     return self.email.split('@')[0]


class UsersFinancials(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='financials')
    companies = models.TextField(blank=True, null=True)
    deposit = models.PositiveSmallIntegerField(blank=True, null=True)
    earnings = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.email
