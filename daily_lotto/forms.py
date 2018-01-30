from django.db.models import F

from daily_lotto.models import *
from django import forms

from tossapp.models import Game


class TicketForm(forms.ModelForm):
    class Meta:
        model = DailyLottoTicket
        exclude = ["id", "ticket_prize", "cost", "purchased_time", "hits", "player_name", "daily_lotto", "tax"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(TicketForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(TicketForm, self).clean()
        n1 = self.cleaned_data.get('n1')
        n2 = self.cleaned_data.get('n2')
        n3 = self.cleaned_data.get('n3')
        n4 = self.cleaned_data.get('n4')
        n5 = self.cleaned_data.get('n5')
        n6 = self.cleaned_data.get('n6')

        Game.objects.filter(name='Daily Lotto').update(times_played=F("times_played") + 1)

        return cleaned_data


class RandomTicketForm(forms.Form):
    quantity = forms.IntegerField(required=False)

    def clean(self):
        cleaned_data = super(RandomTicketForm, self).clean()
        quantity = self.cleaned_data.get('quantity')

        if quantity > 0:
            Game.objects.filter(name='Daily Lotto').update(times_played=F("times_played") + 1)

        return cleaned_data




























