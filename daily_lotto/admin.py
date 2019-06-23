"""
from django.contrib import admin
from daily_lotto.models import *


class DailyLottoAdmin(admin.ModelAdmin):
    list_display = ['lotto_id', 'start_date', 'end_date', 'win1', 'win2', 'win3', 'win4', 'win5', 'win6', 'jack_pot', 'backup_jackpot', ]
    list_filter = ['start_date', 'lotto_type']


class DailyLottoResultAdmin(admin.ModelAdmin):
    search_fields = ['winners']
    list_display = ['winners', 'prize', 'hits_number_prize']
    list_filter = ['winners', 'draw_date']
    list_per_page = 50
    ordering = ['-draw_date']


class DailyLottoTicketAdmin(admin.ModelAdmin):
    search_fields = ['purchased_time', 'id']
    list_filter = ['purchased_time', 'daily_lotto__lotto_type']
    list_display = ['id', 'purchased_time', 'player_name']
    list_per_page = 50


class DailyLottoSumAdmin(admin.ModelAdmin):
    list_display = ('date',)


admin.site.register(DailyLotto, DailyLottoAdmin)
admin.site.register(DailyLottoResult, DailyLottoResultAdmin)
admin.site.register(DailyQuota)
admin.site.register(DailyLottoTicket, DailyLottoTicketAdmin)
admin.site.register(CommissionSum)

"""