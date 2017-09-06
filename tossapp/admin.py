from django.contrib import admin
from daily_lotto.admin import *


# Register your models here.
from tossapp.forms import *
from tossapp.models import Notification, Game_stat, Transaction, Contact_us, Faq, Country


class FaqAdmin(admin.ModelAdmin):
    form = FaqAdminForm
    list_display = ['title', 'detail']


class GameAdmin(admin.ModelAdmin):
    form = GameAdminForm
    list_display = ['name', 'game_photo', 'times_played']

    def game_photo(self, obj):
        if obj.id:
            return '<img src="%s" width="56" height="55">' % obj.display_photo.url
        return ''
    game_photo.allow_tags = True


admin.site.register([Game_stat, Transaction, Notification, Contact_us, Country])
admin.site.register(Faq, FaqAdmin)
admin.site.register(Game, GameAdmin)

