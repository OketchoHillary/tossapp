
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from accounts_api.models import Tuser


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.name, ext)
    return '/'.join(['games', filename])


class Game(models.Model):
    name = models.CharField(max_length=30, unique=True)
    display_photo = models.ImageField(upload_to=content_file_name, default='games/Daily_Lotto.jpg', blank=True, null=True)
    slug = models.SlugField(max_length=230, unique=True)
    times_played = models.BigIntegerField(default=0)

    def __str__(self):
        return self.name


class Game_stat(models.Model):
    LOSE = 0
    WIN = 1
    PENDING = 3
    STATUS_CHOICES = (
        (LOSE, 'Lose'),
        (WIN, 'Win'),
        (PENDING, 'Pending'),
    )
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(Tuser, on_delete=models.CASCADE)
    bet_amount = models.IntegerField()
    status = models.IntegerField(choices=STATUS_CHOICES)
    win_amount = models.FloatField(blank=True, default=0.0)
    loss_amount = models.FloatField(blank=True, default=0.0)
    service_fee = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)

    def __unicode__(self):
        amount = self.win_amount if self.status == self.WIN else self.loss_amount
        return "{} {} {}".format(self.game, self.get_status_display(), amount)

    class Meta:
        ordering = ['-timestamp']
        verbose_name_plural = 'Game statistics'
        verbose_name = 'Game statistic'


class Transaction(models.Model):
    DEPOSIT = 0
    WITHDRAW = 1
    TRANSFER = 2
    TRANSACTION_TYPE_CHOICES = (
        (DEPOSIT, 'Deposit'),
        (WITHDRAW, 'Withdraw'),
        (TRANSFER, 'Transfer'),
    )

    MOBILE_MONEY = 0
    TOSSAPP_TRANSFER = 1
    PAYMENT_METHOD_CHOICES = (
        (MOBILE_MONEY, 'Mobile Money'),
        (TOSSAPP_TRANSFER, 'Tossapp transfer'),
    )

    COMPLETE = 0
    PENDING = 1
    FAILED = 2
    STATUS_CHOICES = (
        (COMPLETE, 'Complete'),
        (PENDING, 'Pending'),
        (FAILED, 'Failed'),
    )
    user = models.ForeignKey(Tuser, on_delete=models.CASCADE)
    reference_no = models.CharField(max_length=13)
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPE_CHOICES)
    payment_method = models.IntegerField(choices=PAYMENT_METHOD_CHOICES)
    amount = models.FloatField(blank=True, default=0.0)
    status = models.IntegerField(choices=STATUS_CHOICES)
    timestamp = models.DateTimeField(editable=False, blank=False)

    def __unicode__(self):
        return "{} {} {}".format(self.reference_no, self.get_transaction_type_display(), self.amount)

    def save(self, *args, **kwargs):
        if not self.id:
            self.timestamp = timezone.localtime(timezone.now())
            return super(Transaction, self).save(*args, **kwargs)

# class Deposit(models.Model):
#     user = models.ForeignKey(Tuser)
#     amount = models.FloatField(blank=True, default=0.0)
#     timestamp = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
#
# class Withdraw(models.Model):
#     user = models.ForeignKey(Tuser)
#     amount = models.FloatField(blank=True, default=0.0)
#     timestamp = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)


class Notification(models.Model):
    id = models.BigAutoField(primary_key=True)
    SUCCESS = 0
    INFORMATION = 1
    WARNING = 2
    ERROR = 3
    ACCOUNT = 4
    STATUS_CHOICES = (
        (SUCCESS, 'Success'),
        (INFORMATION, 'Information'),
        (WARNING, 'Warning'),
        (ERROR, 'Error'),
        (ACCOUNT, 'Account'),
    )
    user = models.ForeignKey(Tuser, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=30)
    description = models.TextField()
    type = models.IntegerField(choices=STATUS_CHOICES, default=INFORMATION)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    seen_status = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

# class Referral(models.Model):
#     user = models.ForeignKey(Tuser)
#     referrer = models.ForeignKey(Tuser)
#     timestamp = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)


# class System_info(models.Model):
#     domain = models.URLField()
#
#     def __unicode__(self):
#         return self.domain
#
#     class Meta:
#         db_table = 'system_info'