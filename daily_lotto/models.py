import datetime
from django.db import models
from django.db.models import BigIntegerField
from django.dispatch import receiver
from django.db.models.signals import post_save
from accounts.models import Tuser
from django.utils import timezone


def now_plus_1():
    return datetime.timedelta(hours=23, minutes=55, seconds=0)


class DailyLotto(models.Model):

    TICKET_PRICE = 500
    HOUSE_COMMISSION_RATE = 0.05
    THREE_SHARE_RATE = 0.10
    FOUR_SHARE_RATE = 0.15
    FIVE_SHARE_RATE = 0.25
    JACKPOT_SHARE_RATE = 0.45

    lotto_id = models.AutoField(primary_key=True)
    start_date = models.DateTimeField(auto_now_add=True, null=False)
    end_date = models.DateTimeField(editable=False, null=False)
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

    def save(self, *args, **kwargs):
        if not self.lotto_id:
            self.end_date = timezone.now() + now_plus_1()
            return super(DailyLotto, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-start_date"]
        db_table = 'lotto'

   # def __str__(self):
         #return '{}, {}, {}, {}, {}, {}'.format(self.win1,self.win2,self.win3,self.win4,self.win5,self.win6)


class DailyQuota(models.Model):
    daily_lotto = models.OneToOneField(DailyLotto, verbose_name="Daily Lotto")
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
    NUMBER_CHOICES = tuple([(i, i,) for i in range(1, 51)])
    n1 = models.IntegerField(verbose_name='Number 1', choices=NUMBER_CHOICES, blank=False, null=False)
    n2 = models.IntegerField(verbose_name='Number 2', choices=NUMBER_CHOICES, blank=False, null=False)
    n3 = models.IntegerField(verbose_name='Number 3', choices=NUMBER_CHOICES, blank=False, null=False)
    n4 = models.IntegerField(verbose_name='Number 4', choices=NUMBER_CHOICES, blank=False, null=False)
    n5 = models.IntegerField(verbose_name='Number 5', choices=NUMBER_CHOICES, blank=False, null=False)
    n6 = models.IntegerField(verbose_name='Number 6', choices=NUMBER_CHOICES, blank=False, null=False)
    ticket_prize = models.IntegerField(default=0)
    hits = models.IntegerField(default=0)
    tax = models.IntegerField(default=0)

    def __str__(self):
        return '{}, {}, {}, {}, {}, {}'.format(self.n1,self.n2,self.n3,self.n4,self.n5,self.n6)

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
    daily_lotto_ticket = models.ForeignKey(DailyLottoTicket)

    def __str__(self):
        return '{:%Y-%m-%d %H:%M}'.format(self.draw_date)

    class Meta:
        db_table = 'lotto_results'


class CommissionSum(models.Model):
    dates = models.DateTimeField(null=False, auto_now_add=True)
    commission_total = models.IntegerField()

    def __str__(self):
        return '{:%Y-%m-%d %H:%M}'.format(self.dates)



