import re
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from accounts_api.models import Tuser, Reset_password


def validate_phone_number(phone):
    match = re.match(r'^(\+?256|0|"+256")7[0578]\d{7}$', phone)
    return match is not None

my_default_errors1 = {
    'required': 'Phone Number is required',
}

my_default_errors2 = {
    'required': 'User Name is required',
}

my_default_errors3 = {
    'required': 'Password is required',
}

my_default_errors4 = {
    'required': 'Retype password is required',
}
my_default_errors5 = {
    'required': 'Select your Gender',
}


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        if not 'initial' in kwargs:
            kwargs['initial'] = {}
        if not 'referrer_share_code' in kwargs['initial']:
            kwargs['initial'].update({'referrer_share_code': None})
        if kwargs['initial']['referrer_share_code'] is not None:
            self.fields['referrer_share_code'].widget.attrs['readonly'] = True
    phone_number = forms.CharField(error_messages=my_default_errors1, widget=forms.TextInput())
    username = forms.CharField(error_messages=my_default_errors2,widget=forms.TextInput())
    password1 = forms.CharField(error_messages=my_default_errors3,widget=forms.PasswordInput())
    password2 = forms.CharField(error_messages=my_default_errors4,widget=forms.PasswordInput())
    referrer_share_code = forms.CharField(max_length=13, required=False, widget=forms.TextInput())
    sex = forms.ChoiceField(error_messages=my_default_errors5, choices=GENDER_CHOICES, required=True)

    class Meta:
        model = Tuser
        fields = ('username', 'phone_number', 'sex')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        if not validate_phone_number(phone_number):
            raise forms.ValidationError("Please provide a valid MTN or Airtel number")
        if phone_number.startswith('0'):
            phone_number = phone_number.replace('0', '256', 1)
        elif phone_number.startswith('+256'):
            phone_number = phone_number.replace('+256', '256', 1)
        return phone_number

    def clean_referrer(self):
        if len(Tuser.objects.filter(share_code=self.cleaned_data.get("referrer_share_code"))) == 0:
            raise forms.ValidationError("Please provide a valid username or leave the field blank")
        return self.cleaned_data.get("referrer")

    def save(self, commit=True):
        gender = self.cleaned_data.get('sex')
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.sex = self.cleaned_data["sex"]
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = False
        self.fields['last_name'].required = False
        self.fields['sex'].required = False
        self.fields['country'].required = False
        self.fields['address'].required = False
        self.fields['profile_photo'].required = False
        self.fields['dob'].required = False

    password = ReadOnlyPasswordHashField(label="Password",
                                         help_text=(
                                             "Raw passwords are not stored, so there is no way to see this "
                                             "user's password, but you can change the password using "
                                             "<a href=\"../password/\">this form</a>."
                                         ),
                                         )

    class Meta:
        model = Tuser
        fields = ('username', 'password', 'phone_number', 'referrer', 'is_active', 'is_admin', 'share_code', 'dob')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        if not validate_phone_number(phone_number):
            raise forms.ValidationError("Please provide a valid MTN or Airtel number")
        if phone_number.startswith('0'):
            phone_number = phone_number.replace('0', '+256', 1)
        elif phone_number.startswith('256'):
            phone_number = phone_number.replace('256' '+256', 1)
        return phone_number


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'phone_number', 'is_admin', 'timestamp', 'sex', 'balance')
    list_filter = ('is_admin', 'sex', 'last_login')
    search_fields = ('username', )
    fieldsets = (
        (None, {'fields': ('username','phone_number','referrer', 'password',)}),
        ('Personal info', {'fields': ('first_name','last_name','sex','country','address','profile_photo','dob')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'phone_number', 'password1', 'password2', 'referrer_share_code',)}
        ),
    )
    ordering = ('id',)
    filter_horizontal = ()

# Now register the new UserAdmin...
admin.site.register(Tuser, UserAdmin)
admin.site.register(Reset_password)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)