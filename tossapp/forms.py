from django import forms
from django.core.exceptions import ValidationError
from django.utils.text import slugify

from accounts.models import Tuser
from tossapp.models import Faq, Contact_us, Game, Transaction, Notification
from django_countries import countries
from accounts.admin import validate_phone_number
# import yopayments


my_default_errors1 = {
    'required': 'Old password is required',
}

my_default_errors2 = {
    'required': 'New password is required',
}

my_default_errors3 = {
    'required': 'Please Retype New password',
}

my_default_errors4 = {
    'required': 'Your name is required',
}

my_default_errors5 = {
    'required': 'Your email is required',
}

my_default_errors6 = {
    'required': 'Your subject',
}

my_default_errors7 = {
    'required': 'Your Message is required',
}


class ChangeUsernameForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ChangeUsernameForm, self).__init__(*args, **kwargs)

    current_username = forms.CharField(max_length=15, widget=forms.TextInput())
    new_username = forms.CharField(max_length=15, widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_new_username(self):
        new_username = self.cleaned_data['new_username']
        qs = Tuser.objects.filter(username=new_username)
        # if self.id:
        #     qs = qs.exclude(pk=self.id)
        if qs.count() > 0:
            raise ValidationError('This username is already in use.')
        return new_username


class ChangePasswordForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

    old_password = forms.CharField(error_messages=my_default_errors1, widget=forms.PasswordInput())
    new_password = forms.CharField(error_messages=my_default_errors2, widget=forms.PasswordInput())
    retype_new_password = forms.CharField(error_messages=my_default_errors3,widget=forms.PasswordInput())

    def clean_old_password(self):
        old_password = self.cleaned_data.get("old_password", None)
        if not self.user.check_password(old_password):
            raise ValidationError('Incorrect password.')
        return old_password
        # return user if user.check_password(password) else None

    def clean_retype_new_password(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("new_password")
        password2 = self.cleaned_data.get("retype_new_password")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


class ChangeProfileForm(forms.ModelForm):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    Country = tuple(countries)
    COUNTRY_CHOICES = [('UG', 'Uganda')] + list(Country)

    first_name = forms.CharField(widget=forms.TextInput(), required=False)
    last_name = forms.CharField(widget=forms.TextInput(), required=False)
    phone_number = forms.CharField(widget=forms.TextInput(), required=False)
    sex = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(), required=False)
    country = forms.ChoiceField(choices=COUNTRY_CHOICES, widget=forms.Select(attrs={'class':'form-control'}), required=False)
    address = forms.CharField(widget=forms.TextInput(), required=False)

    class Meta:
        model = Tuser
        fields = ['first_name', 'last_name', 'phone_number', 'sex', 'country', 'address']

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        if not validate_phone_number(phone_number):
            raise forms.ValidationError("Please provide a valid MTN or Airtel number")
        if phone_number.startswith('0'):
            phone_number = phone_number.replace('0','256',1)
        return phone_number

    def clean_details(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        sex = self.cleaned_data.get('sex')
        country = self.cleaned_data.get('country')
        address = self.cleaned_data.get('address')

    def save(self, commit=True):
        phone_number = self.cleaned_data.get("phone_number")
        if not validate_phone_number(phone_number):
            raise forms.ValidationError("Please provide a valid MTN or Airtel number")
        if phone_number.startswith('0'):
            phone_number = phone_number.replace('0', '256', 1)
        user = super(ChangeProfileForm, self).save(commit=False)
        user.phone_number = phone_number
        if commit:
            user.save()
        return user


class ChangeDpForm(forms.ModelForm):
    profile_photo = forms.ImageField(required=False)

    class Meta:
        model = Tuser
        fields = ['profile_photo']

    def clean_details(self):
        profile_photo = self.cleaned_data.get('profile_photo')


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact_us
        fields = ['your_name', 'your_email', 'your_message']

    def clean_contact(self):
        your_name = self.cleaned_data.get('your_name')
        your_email = self.cleaned_data.get('your_email')
        your_message = self.cleaned_data.get('your_message')

    def save(self, commit=True):
        instance = super(ContactForm, self).save(commit=False)
        instance.save()
        return instance


class FaqAdminForm(forms.ModelForm):
    class Meta:
        model = Faq
        fields = ('question', 'answer',)

    def save(self, commit=True):
        instance = super(FaqAdminForm, self).save(commit=False)
        instance.slug = slugify(instance.question)
        instance.save()
        return instance


class GameAdminForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('name', 'display_photo')

    def save(self, commit=True):
        instance1 = super(GameAdminForm, self).save(commit=False)
        instance1.slug = slugify(instance1.name)
        instance1.save()
        return instance1


class DepoForm(forms.Form):

    def clean_details(self):
        number = self.cleaned_data.get('number')
        amount = self.cleaned_data.get('amount')
        YoPay = yopayments.YoPay("90001817196", "1261050237")
        api_url = "https://41.220.12.206/services/yopaymentsdev/task.php"
        YoPay.set_non_blocking(False)
        response = YoPay.ac_deposit_funds(number, amount, "reason for payment")
        if response.get("TransactionStatus") == "SUCCEEDED":
            print('success')
        else:
            raise forms.ValidationError("wrong input")


class Update_notice(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['seen_status']

"""
class WithdrawForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(WithdrawForm, self).__init__(*args, **kwargs)

    def clean_details(self):
        number = self.cleaned_data.get('number')
        amount = self.cleaned_data.get('amount')
        YoPay = yopayments.YoPay(90001817196, 1261050237)
        YoPay.set_non_blocking(True)
        response = YoPay.ac_deposit_funds(number, amount, "reason for payment")
        if response.get("TransactionStatus") == "SUCCEEDED":
            print 'success'
        else:
            raise forms.ValidationError("wrong input")
            Payment failed
	        """




