from daily_lotto.models import *
from django import forms


class TicketForm(forms.ModelForm):
    class Meta:
        model = DailyLottoTicket
        exclude = ["user_id","ticket_prize", "cost", "purchased_time", "hits", "player_name", "daily_lotto"]


class RandomTicketForm(forms.Form):
    quantity = forms.IntegerField(required=False, label='Quantity of random Tickets:',
                                  widget=forms.NumberInput(attrs={'max': 500, 'min': 1, 'placeholder': 'random tickets'}))

























