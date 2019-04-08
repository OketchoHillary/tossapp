from __future__ import unicode_literals

import random

from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.
from django.db.models import Count
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django_countries.fields import Country, CountryField
from rest_framework.authtoken.models import Token
# from django.utils import timezone


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.username, ext)
    return '/'.join(['users', filename])


def toss_share_code():
    m_code = ""
    for x in range(6):
        m_code = m_code + str(random.randint(0, 9))
    return str(m_code)


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
    username = models.CharField(max_length=15, unique=True, error_messages={'unique':"A user with this username already exists."})
    phone_number = models.CharField(max_length=13, unique=True, error_messages={'unique':"A user with this phone number already exists."})
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES)
    country = CountryField(null=True)
    address = models.CharField(max_length=30)
    referrer = models.ForeignKey('self', blank=True, related_name='referrals', null=True)
    referrer_prize = models.IntegerField(editable=False, default=0)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False, blank=False)
    profile_photo = models.ImageField(upload_to=content_file_name, default='default_avatar/avatar.png')
    points = models.IntegerField(default=0)
    redeemed_points = models.IntegerField(default=0)
    balance = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    verification_code = models.CharField(default='',blank=True, max_length=6)
    share_code = models.CharField(max_length=6, blank=True, unique=True,
                                  validators=[RegexValidator(regex='^.{6}$',
                                                             message='Share code must not exceed 6 characters',
                                                             code=None)])

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

    def tossapp_ranking(self):
        aggregate = Tuser.objects.filter(points__gt=self.points).aggregate(tossapp_ranking=Count('points'))
        return aggregate['tossapp_ranking'] + 1

    @property
    def refferal_ranking(self):
        rTusers = Tuser.objects.annotate(num_ref=Count('referrals'))
        num_ref = rTusers.get(username=self.username).num_ref
        referals = rTusers.filter(num_ref__gt=num_ref).aggregate(refferal_ranking=Count('num_ref'))
        return referals['refferal_ranking'] + 1

    def __str__(self):             # __unicode__ on Python 2
        return self.username

    def save(self, *args, **kwargs):
        if not self.id:
            self.timestamp = timezone.localtime(timezone.now())
            while True:
                my_code = toss_share_code()
                if not Tuser.objects.filter(share_code=my_code).exists():
                    break
            self.share_code = toss_share_code()
        return super(Tuser, self).save(*args, **kwargs)

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


@receiver(post_save, sender=Tuser)
def create_auth_token(sender, created, instance, **kwargs):
        if created:
            token = Token(user=instance)
            token.save()


"""
        def restore_objects(self, attrs, instance=None):
            if instance is not None:
                instance.tuser.username = attrs.get('user.username', instance.tuser.username)
                instance.tuser.phone_number = attrs.get('user.phone_number', instance.tuser.phone_number)
                instance.tuser.sex = attrs.get('user.sex', instance.tuser.sex)
                instance.tuser.password = attrs.get('user.password', instance.tuser.password)
            user = Tuser.objects.create(username=attrs.get('user.username'), phone_number=attrs.get('user.phone_number'), sex=attrs.get('user.sex'), password=attrs.get('user.password'))
            return Tuser(user=user)
"""