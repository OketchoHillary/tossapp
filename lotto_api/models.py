import random
import string
from datetime import *
from django.utils import timezone
from django.db import models, IntegrityError
from django.dispatch import receiver
from django.db.models.signals import post_save
from accounts_api.models import Tuser
from tauth.settings import NUMBER_RANGE


# daily lotto end date and time
def now_plus_1():
    return timedelta(hours=23, minutes=55, seconds=0)


# quarterly day lotto end date and time
def now_plus_2():
    return timedelta(hours=5, minutes=55)


# hourly day lotto end date and time
def now_plus_3():
    return timedelta(minutes=55)


def create_unique_id():
    return ''.join(random.choices(string.digits, k=8))


class DailyLotto(models.Model):

    TICKET_PRICE = 500
    HOUSE_COMMISSION_RATE = 0.05
    THREE_SHARE_RATE = 0.10
    FOUR_SHARE_RATE = 0.15
    FIVE_SHARE_RATE = 0.25
    JACKPOT_SHARE_RATE = 0.45
    LOTTO_TYPE = (
        ('D', 'Daily'),
        ('H', 'Hourly'),
        ('Q', 'Quarterly'),
    )

    lotto_id = models.AutoField(primary_key=True)
    lotto_type = models.CharField(max_length=1, choices=LOTTO_TYPE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    win1 = models.IntegerField(default=0)
    win2 = models.IntegerField(default=0)
    win3 = models.IntegerField(default=0)
    win4 = models.IntegerField(default=0)
    win5 = models.IntegerField(default=0)
    win6 = models.IntegerField(default=0)
    jack_pot = models.IntegerField(default=0)
    backup_jackpot = models.IntegerField(default=0)

    def __str__(self):
        return '{:%Y-%m-%d %H:%M}'.format(self.start_date)

    class Meta:
        ordering = ["-lotto_id"]
        db_table = 'lotto'

    def save(self, *args, **kwargs):

        if not self.lotto_id:
            self.start_date = timezone.now()
        return super(DailyLotto, self).save(*args, **kwargs)


class DailyQuota(models.Model):
    daily_lotto = models.OneToOneField(DailyLotto, on_delete=models.CASCADE, verbose_name="Daily Lotto")
    house_commission = models.IntegerField(default=0)
    six_number_prize_pool = models.IntegerField(default=0)
    five_number_prize_pool = models.IntegerField(default=0)
    four_number_prize_pool = models.IntegerField(default=0)
    three_number_prize_pool = models.IntegerField(default=0)
    six_number_prize_pool_commission = models.IntegerField(default=0)
    five_number_prize_pool_commission = models.IntegerField(default=0)
    four_number_prize_pool_commission = models.IntegerField(default=0)
    three_number_prize_pool_commission = models.IntegerField(default=0)

    def __str__(self):
        return str(self.daily_lotto)

    @receiver(post_save, sender=DailyLotto)
    def create_quota_for_new_lotto(sender, created, instance, **kwargs):
        if created:
            daily_quota = DailyQuota(daily_lotto=instance)
            daily_quota.save()

    class Meta:
        db_table = 'quotas'


class DailyLottoTicket(models.Model):
    id = models.BigAutoField(primary_key=True)
    player_name = models.ForeignKey(Tuser, on_delete=models.CASCADE)
    daily_lotto = models.ForeignKey(DailyLotto, on_delete=models.CASCADE)
    cost = models.IntegerField(default=500)
    purchased_time = models.DateTimeField(auto_now_add=True, editable=False)
    NUMBER_CHOICES = tuple([(i, i,) for i in range(1, NUMBER_RANGE)])
    n1 = models.IntegerField(verbose_name='Number 1', choices=NUMBER_CHOICES, blank=False, null=False)
    n2 = models.IntegerField(verbose_name='Number 2', choices=NUMBER_CHOICES, blank=False, null=False)
    n3 = models.IntegerField(verbose_name='Number 3', choices=NUMBER_CHOICES, blank=False, null=False)
    n4 = models.IntegerField(verbose_name='Number 4', choices=NUMBER_CHOICES, blank=False, null=False)
    n5 = models.IntegerField(verbose_name='Number 5', choices=NUMBER_CHOICES, blank=False, null=False)
    n6 = models.IntegerField(verbose_name='Number 6', choices=NUMBER_CHOICES, blank=False, null=False)
    ticket_prize = models.IntegerField(default=0)
    hits = models.IntegerField(default=0)
    tax = models.IntegerField(default=0)
    ticket_no = models.CharField(max_length=8, blank=True, null=True)

    def __str__(self):
        return '{}, {}, {}, {}, {}, {}'.format(self.n1,self.n2,self.n3,self.n4,self.n5,self.n6)

    def save(self, *args, **kwargs):
        m = ''.join(random.choices(string.digits, k=8))
        self.ticket_no = m
        try:
            DailyLottoTicket.objects.filter(ticket_no=m).exists()
        except IntegrityError:
            self.ticket_no = create_unique_id()

        return super(DailyLottoTicket, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Daily Lotto Tickets"
        db_table = 'lotto_tickets'
        ordering = ['-purchased_time', ]


class DailyLottoResult(models.Model):
    daily_lotto = models.ForeignKey(DailyLotto, on_delete=models.CASCADE)
    draw_date = models.DateTimeField(auto_now_add=True, null=False, editable=False)
    winners = models.CharField(max_length=177)
    hits_number_prize = models.IntegerField()
    service_commission = models.IntegerField(default=25)
    prize = models.IntegerField()
    daily_lotto_ticket = models.ForeignKey(DailyLottoTicket, on_delete=models.CASCADE)

    def __str__(self):
        return '{:%Y-%m-%d %H:%M}'.format(self.draw_date)

    class Meta:
        db_table = 'lotto_results'


class CommissionSum(models.Model):
    dates = models.DateTimeField(null=False, auto_now_add=True)
    commission_total = models.IntegerField()

    def __str__(self):
        return '{:%Y-%m-%d %H:%M}'.format(self.dates)

    class Meta:
        db_table = 'lotto_commission'

