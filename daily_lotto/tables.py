"""
import django_tables2 as tables
from daily_lotto.models import DailyLottoTicket


class TicketTable(tables.Table):
    class Meta:
        model = DailyLottoTicket
        fields = ['purchased_time', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6']
        attrs = {'class': 'table table-striped table-bordered table-hover'}
        """
