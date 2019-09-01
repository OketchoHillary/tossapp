
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import truncatechars
from django.urls import reverse

from accounts_api.models import Tuser


class Contact_us(models.Model):
    your_name = models.CharField(max_length=30, blank=False, null=False)
    your_email = models.EmailField(blank=False)
    your_message = models.TextField(max_length=1000, blank=False, null=False)

    @property
    def short_text(self):
        return truncatechars(self.your_message, 15)

    class Meta:
        db_table = 'Contact Us'
        verbose_name_plural = "Contact Us Messages"


class Faq(models.Model):
    question = models.CharField(max_length=230)
    slug = models.SlugField(max_length=230, unique=True)
    answer = models.TextField(max_length=100)

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse('faq-view', args=(self.slug, ))

    class Meta:
        verbose_name_plural = 'Faq'
        ordering = ['question']

