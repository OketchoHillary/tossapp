from django import forms
from django.core.exceptions import ValidationError
from django.utils.text import slugify

from accounts.models import Tuser
from tossapp.models import Faq, Contact_us, Game
from django_countries import countries
from accounts.admin import validate_phone_number

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
        old_password = self.cleaned_data.get("old_password")
        if not self.user.check_password(old_password):
            raise ValidationError('Incorrect password.')
        return old_password
        # return user if user.check_password(password) else Non

    def clean_retype_new_password(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("new_password")
        password2 = self.cleaned_data.get("retype_new_password")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


class ChangeProfileForm(forms.Form):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    Country = tuple(countries)
    COUNTRY_CHOICES = tuple(Country)

    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    phone_number = forms.CharField(widget=forms.TextInput())
    sex = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select())
    country = forms.ChoiceField(choices=COUNTRY_CHOICES, widget=forms.Select())
    address = forms.CharField(widget=forms.TextInput())

    class Meta:
        modle = Tuser
        fields = ['first_name', 'last_name', 'phone_number', 'sex', 'country', 'address']

    def __init__(self, *args, **kwargs):
        super(ChangeProfileForm, self).__init__(*args, **kwargs)

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
        # Save the provided password in hashed format
        user = super(ChangeProfileForm, self).save(commit=False)
        user.phone_number = self.cleaned_data['phone_number']
        if commit:
            user.save()
        return user


class ContactForm(forms.ModelForm):
    your_name = forms.CharField(required=True, error_messages=my_default_errors4, widget=forms.TextInput(attrs={'class':'form-control', 'size':'10','placeholder':'Your name'}))
    your_email = forms.CharField(required=True,error_messages=my_default_errors5, widget=forms.EmailInput(attrs={'class':'form-control', 'size':'10','placeholder':'Your email'}))
    your_subject = forms.CharField(required=True,error_messages=my_default_errors6, widget=forms.TextInput(attrs={'class':'form-control', 'size':'10','placeholder':'Your subject'}))
    your_message = forms.CharField(required=True,error_messages=my_default_errors7, widget=forms.Textarea(attrs={'class':'form-control', 'size':'10','placeholder':'Your message'}))

    class Meta:
        model = Contact_us
        fields = ['your_name', 'your_email', 'your_subject', 'your_message']



class FaqAdminForm(forms.ModelForm):
    class Meta:
        model = Faq
        fields = ('title', 'detail',)

    def save(self, commit=True):
        instance = super(FaqAdminForm, self).save(commit=False)
        instance.slug = slugify(instance.title)
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