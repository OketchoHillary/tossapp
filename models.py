# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountsApiResetPassword(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    expiry = models.DateTimeField()
    reset_code = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'accounts_api_reset_password'


class AskappAnswer(models.Model):
    answer_text = models.CharField(max_length=200)
    question_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'askapp_answer'


class AskappQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'askapp_question'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user_id = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class ContactUs(models.Model):
    your_name = models.CharField(max_length=30)
    your_email = models.CharField(max_length=254)
    your_message = models.TextField()

    class Meta:
        managed = False
        db_table = 'contact us'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Lotto(models.Model):
    lotto_id = models.AutoField(primary_key=True)
    lotto_type = models.CharField(max_length=1)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    win1 = models.IntegerField()
    win2 = models.IntegerField()
    win3 = models.IntegerField()
    win4 = models.IntegerField()
    win5 = models.IntegerField()
    win6 = models.IntegerField()
    jack_pot = models.IntegerField()
    backup_jackpot = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lotto'


class LottoCommission(models.Model):
    dates = models.DateTimeField()
    commission_total = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lotto_commission'


class LottoResults(models.Model):
    draw_date = models.DateTimeField()
    winners = models.CharField(max_length=177)
    hits_number_prize = models.IntegerField()
    service_commission = models.IntegerField()
    prize = models.IntegerField()
    daily_lotto_id = models.IntegerField()
    daily_lotto_ticket_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'lotto_results'


class LottoTickets(models.Model):
    id = models.BigAutoField(primary_key=True)
    cost = models.IntegerField()
    purchased_time = models.DateTimeField()
    n1 = models.IntegerField()
    n2 = models.IntegerField()
    n3 = models.IntegerField()
    n4 = models.IntegerField()
    n5 = models.IntegerField()
    n6 = models.IntegerField()
    ticket_prize = models.IntegerField()
    hits = models.IntegerField()
    tax = models.IntegerField()
    daily_lotto_id = models.IntegerField()
    player_name_id = models.IntegerField()
    ticket_no = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lotto_tickets'


class Quotas(models.Model):
    house_commission = models.IntegerField()
    six_number_prize_pool = models.IntegerField()
    five_number_prize_pool = models.IntegerField()
    four_number_prize_pool = models.IntegerField()
    three_number_prize_pool = models.IntegerField()
    six_number_prize_pool_commission = models.IntegerField()
    five_number_prize_pool_commission = models.IntegerField()
    four_number_prize_pool_commission = models.IntegerField()
    three_number_prize_pool_commission = models.IntegerField()
    daily_lotto_id = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'quotas'


class SystemInfo(models.Model):
    domain = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'system_info'


class TossappApiGame(models.Model):
    name = models.CharField(unique=True, max_length=30)
    display_photo = models.CharField(max_length=100, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=230)
    times_played = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tossapp_api_game'


class TossappApiGameStat(models.Model):
    bet_amount = models.IntegerField()
    status = models.IntegerField()
    win_amount = models.FloatField()
    loss_amount = models.FloatField()
    service_fee = models.FloatField()
    timestamp = models.DateTimeField()
    game_id = models.IntegerField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tossapp_api_game_stat'


class TossappApiNotification(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.TextField()
    type = models.IntegerField()
    timestamp = models.DateTimeField()
    seen_status = models.IntegerField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tossapp_api_notification'


class TossappApiTransaction(models.Model):
    reference_no = models.CharField(max_length=13)
    transaction_type = models.IntegerField()
    payment_method = models.IntegerField()
    amount = models.FloatField()
    status = models.IntegerField()
    timestamp = models.DateTimeField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tossapp_api_transaction'


class TossappFaq(models.Model):
    question = models.CharField(max_length=230)
    slug = models.CharField(unique=True, max_length=230)
    answer = models.TextField()

    class Meta:
        managed = False
        db_table = 'tossapp_faq'


class Users(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    username = models.CharField(unique=True, max_length=15)
    phone_number = models.CharField(unique=True, max_length=15)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    sex = models.CharField(max_length=1, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=2, blank=True, null=True)
    address = models.CharField(max_length=30)
    referrer_prize = models.IntegerField()
    timestamp = models.DateTimeField()
    profile_photo = models.CharField(max_length=100)
    balance = models.IntegerField()
    is_active = models.IntegerField()
    is_admin = models.IntegerField()
    verification_code = models.CharField(max_length=6)
    is_agreed = models.IntegerField()
    share_code = models.CharField(unique=True, max_length=6)
    referrer_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
