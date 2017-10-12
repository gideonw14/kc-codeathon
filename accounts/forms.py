from datetime import datetime
from django.contrib.auth import forms as auth_forms

from django import forms
from django.contrib.auth.models import User

from accounts.models import Profile
import accounts.constants as const


class Register(auth_forms.UserCreationForm):
    email = forms.EmailField(required=True, max_length=const.EMAIL_MAX)
    first_name = forms.CharField(max_length=const.USERNAME_MAX)
    last_name = forms.CharField(max_length=const.USERNAME_MAX)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name',
                  'last_name')

    def __init__(self, *args, **kwargs):
        super(Register, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = None

    def clean_username(self):
        data = self.cleaned_data['username']
        if User.objects.filter(username=data).exists():
            raise forms.ValidationError("This username is already taken.",
                                        code='unique_username')
        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("This email is already in use.",
                                        code='unique_email')
        return data

    def save(self, commit=True):
        user = super(Register, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.is_active = False
        if commit:
            user.save()
        profile = Profile()
        profile.user = user
        profile.key_expires = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
        profile.save()
        return user


class EditUser(forms.Form):
    first_name = forms.CharField(required=False, max_length=const.USERNAME_MAX)
    last_name = forms.CharField(required=False, max_length=const.USERNAME_MAX)
    email = forms.EmailField(required=False, max_length=const.EMAIL_MAX)

    def is_valid(self, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs['user']
        return super(EditUser, self).is_valid()


    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            user = User.objects.get(email=data)
            if not user.username == self.user.username:
                raise forms.ValidationError("This email is already in use.",
                                        code='unique_email')
        return data


class ChangePassword(auth_forms.PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(ChangePassword, self).__init__(*args, **kwargs)

        for fieldname in ['new_password1', 'new_password2']:
            self.fields[fieldname].help_text = None


class PasswordSet(auth_forms.SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(PasswordSet, self).__init__(*args, **kwargs)

        for fieldname in ['new_password1', 'new_password2']:
            self.fields[fieldname].help_text = None