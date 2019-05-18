"""
from django.contrib import admin
from daily_lotto.admin import *


# Register your models here.
from tossapp.forms import *
from tossapp.models import Notification, Game_stat, Transaction, Contact_us, Faq


class FaqAdmin(admin.ModelAdmin):
    form = FaqAdminForm
    list_display = ['question', 'answer']


class GameAdmin(admin.ModelAdmin):
    form = GameAdminForm
    list_display = ['name', 'game_photo', 'times_played']

    def game_photo(self, obj):
        if obj.id:
            return '<img src="%s" width="56" height="55">' % obj.display_photo.url
        return ''
    game_photo.allow_tags = True
    


class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'reference_no', 'transaction_type', 'payment_method', 'amount', 'status', 'timestamp']
    list_per_page = 100
    list_filter = ['transaction_type', 'payment_method', 'status', 'timestamp']
    search_fields = ['reference_no']


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['short_text']


admin.site.register([Game_stat, Notification])
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Faq, FaqAdmin)
admin.site.register(Contact_us, ContactUsAdmin)

"""