from django import forms
from django.core.exceptions import ValidationError
from django.utils.text import slugify

from accounts.models import Tuser
from tossapp.models import Faq


my_default_errors1 = {
    'required': 'Old password is required',
}

my_default_errors2 = {
    'required': 'New password is required',
}

my_default_errors3 = {
    'required': 'Please Retype New password',
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

class FaqAdminForm(forms.ModelForm):
    class Meta:
        model = Faq
        fields = ('title', 'detail',)

    def save(self, commit=True):
        instance = super(FaqAdminForm, self).save(commit=False)
        instance.slug = slugify(instance.title)
        instance.save()
        return instance