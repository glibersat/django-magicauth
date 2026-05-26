from django import forms
from django.contrib.auth import get_user_model
from django.utils.module_loading import import_string

from magicauth import settings as magicauth_settings
from . import adapters


class EmailForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        user_email = self.cleaned_data["email"]

        email_field = magicauth_settings.EMAIL_FIELD
        field_lookup = {f"{email_field}__iexact": user_email}

        if not get_user_model().objects.filter(**field_lookup).exists():
            adapter = adapters.get_adapter()
            adapter.email_unknown_callback(user_email, self)

        return user_email
