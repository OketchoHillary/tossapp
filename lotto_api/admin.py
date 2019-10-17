
from django.contrib import admin

from lotto_api.models import DailyLotto, DailyLottoResult, DailyQuota, DailyLottoTicket, CommissionSum


class DailyLottoAdmin(admin.ModelAdmin):
    list_display = ['lotto_id', 'start_date', 'end_date', 'win1', 'win2', 'win3', 'win4', 'win5', 'win6', 'jack_pot',
                    'backup_jackpot', ]
    list_filter = ['start_date', 'lotto_type']


class DailyLottoResultAdmin(admin.ModelAdmin):
    search_fields = ['winners']
    list_display = ['winners', 'prize', 'hits_number_prize']
    list_filter = ['hits_number_prize', 'draw_date']
    list_per_page = 50
    ordering = ['-draw_date']


class DailyLottoTicketAdmin(admin.ModelAdmin):
    search_fields = ['purchased_time', 'id']
    list_filter = ['purchased_time', 'daily_lotto__lotto_type']
    list_display = ['id', 'ticket_no', 'purchased_time', 'player_name']
    list_per_page = 50


class DailyLottoSumAdmin(admin.ModelAdmin):
    list_display = ('date',)


class DailyQuotaAdmin(admin.ModelAdmin):
    list_filter = ['daily_lotto__lotto_type', 'daily_lotto__start_date']
    list_display = ['three_number_prize_pool', 'four_number_prize_pool',
                    'five_number_prize_pool', 'six_number_prize_pool',
                    'three_number_prize_pool']


admin.site.register(DailyLotto, DailyLottoAdmin)
admin.site.register(DailyLottoResult, DailyLottoResultAdmin)
admin.site.register(DailyQuota, DailyQuotaAdmin)
admin.site.register(DailyLottoTicket, DailyLottoTicketAdmin)
admin.site.register(CommissionSum)

