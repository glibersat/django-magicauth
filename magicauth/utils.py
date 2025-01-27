import binascii
import importlib
import os

from django import forms

from . import settings as magicauth_settings


def generate_token():
    return binascii.hexlify(os.urandom(20)).decode()


def raise_error(email=None):
    """
    Just raise an error - this can be used as a call back function
    when no user was found in DB during the login process.
    """
    raise forms.ValidationError(magicauth_settings.EMAIL_UNKNOWN_MESSAGE)


def import_attribute(path):
    """Stolen from https://github.com/pennersr/django-allauth/blob/master/allauth/utils.py"""
    assert isinstance(path, str)
    pkg, attr = path.rsplit(".", 1)
    return getattr(importlib.import_module(pkg), attr)
