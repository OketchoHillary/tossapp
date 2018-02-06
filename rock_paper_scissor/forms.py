from django import forms


class R_P_S_Form(forms.Form):
    accountBalance = forms.IntegerField()