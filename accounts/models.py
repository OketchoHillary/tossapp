from __future__ import unicode_literals

import datetime
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.
from django_countries.fields import Country, CountryField
# from django.utils import timezone


class TuserManager(BaseUserManager):
    def create_user(self, username, phone_number, password=None):
        """
        Creates and saves a User with the given username, phone number and password.
        """
        if not username:
            raise ValueError('Users must have a username')

        if not phone_number:
            raise ValueError('Users must have a phone number')

        user = self.model(
            username=username,
            phone_number=phone_number
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, phone_number, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username,
            phone_number=phone_number,
            password=password,
        )
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user


class Tuser(AbstractBaseUser):
    REFERRAL_PRIZE = 50
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    username = models.CharField(max_length=15,unique=True, error_messages={'unique':"A user with this username already exists."})
    phone_number = models.CharField(max_length=13,unique=True,error_messages={'unique':"A user with this phone number already exists."})
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    sex = models.CharField(max_length=1,choices=GENDER_CHOICES)
    country = CountryField()
    address = models.CharField(max_length=30)
    referrer = models.ForeignKey('self', blank=True, related_name='referrals', null=True)
    referrer_prize = models.IntegerField(editable=False, default=0)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False, blank=False)
    profile_photo = models.ImageField(upload_to='users', default='default_avatar/avatar.png')
    points = models.IntegerField(default=0)
    redeemed_points = models.IntegerField(default=0)
    balance = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    verification_code = models.CharField(default='',blank=True, max_length=6)

    objects = TuserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone_number']

    def get_full_name(self):
        # The user is identified by their username
        return self.username

    def get_my_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        # The user is identified by their username
        return self.username

    def __str__(self):             # __unicode__ on Python 2
        return self.username

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        ordering = ['points']
