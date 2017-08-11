from django.contrib import admin
from daily_lotto.admin import *


# Register your models here.
from tossapp.forms import FaqAdminForm
from tossapp.models import Notification, Game_stat, Game, Transaction, Contact_us, Faq


class FaqAdmin(admin.ModelAdmin):
    form = FaqAdminForm
    list_display = ['title', 'detail']

admin.site.register([Game, Game_stat, Transaction, Notification, Contact_us])
admin.site.register(Faq, FaqAdmin)
