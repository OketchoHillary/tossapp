from django import forms
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from django.urls import reverse_lazy
from django.db.models import F
from django.http import HttpResponseRedirect

from accounts.admin import validate_phone_number
from accounts.models import Tuser
# from accounts.sendSms import send_verification_sms
from accounts.utils import generate_verification_code
#from tossapp.models import Notification


class AuthForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class ForgotLoginPassForm(forms.Form):
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Phone Number', 'id':'phone'}))

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        if not validate_phone_number(phone_number):
            raise forms.ValidationError("Please provide a valid MTN or Airtel number")
        if phone_number.startswith('0'):
            phone_number = phone_number.replace('0','256',1)
        if len(Tuser.objects.filter(phone_number=phone_number)) == 0:
            raise forms.ValidationError("We cannot find an account associated with this phone number")
        return phone_number


class ActivationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ActivationForm, self).__init__(*args, **kwargs)

    verification_code = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'class':'form-control'}))

    def clean_verification_code(self):
        code = self.cleaned_data.get('verification_code')
        if self.user and self.user.verification_code == code:
            Notification.objects.create(user=self.user, title='Welcome to Tossapp',
                                        description='You have successfully created your Tossapp account.',
                                        type=0)
            # Getting shared code of sponsor
            sponsor_code = Tuser.objects.filter(id=self.user.id).values_list('referrer_id')[0]
            x = int(sponsor_code[0])
            Tuser.objects.filter(id=x).update(referrer_prize=F("referrer_prize") + Tuser.REFERRAL_PRIZE,
                                              balance=F("balance") + Tuser.REFERRAL_PRIZE)
            # incrementing points on referee
            Tuser.objects.filter(id=x).update(points=F("points") + 1)
            # user.referrer_prize = Tuser.REFERRAL_PRIZE
            
            return code
        else:
            raise forms.ValidationError(u'Wrong verification code.')
        # if UserProfile.objects.filter(email=email).count():
        #     raise forms.ValidationError(u'That email address already exists.')
        # return email


class NewCodeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(NewCodeForm, self).__init__(*args, **kwargs)

    verification_code = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_verification_code(self):
        code = self.cleaned_data.get('verification_code')
        if self.user and self.user.verification_code == code:
            return code
        else:
            raise forms.ValidationError(u'Wrong verification code.')


class NewPassForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput())
    new_password2 = forms.CharField(widget=forms.PasswordInput())


class ChangeNumberForm(forms.Form):
    phone_number = forms.CharField(max_length=13, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone Number'}))

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        if not validate_phone_number(phone_number):
            raise forms.ValidationError("Please provide a valid MTN or Airtel number")
        if phone_number.startswith('0'):
            phone_number = phone_number.replace('0','256',1)
        if len(Tuser.objects.filter(phone_number=phone_number)) != 0:
            raise forms.ValidationError("This phone number is already registered with another user.")
        return phone_number


# class TactivationForm(AuthenticationForm):
#     def confirm_login_allowed(self, user):
#         if not user.is_active:
#             tuser = user
#             code = generate_verification_code()
#             tuser.verification_code = code
#             tuser.save()
#             # send_verification_sms(tuser.phone_number,tuser.verification_code)
#             HttpResponseRedirect(reverse_lazy('activate', kwargs={'user': tuser.username}))
#             # return HttpResponseRedirect(reverse_lazy('activate', kwargs={'user': tuser.username}))
#             # raise forms.ValidationError(
#             #     _("Your account has expired. \
#             #     Please click the renew subscription link below"),
#             #     code='inactive',
#             # )


