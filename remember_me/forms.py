from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _


class AuthenticationRememberMeForm(AuthenticationForm):

    """
    Subclass of Django ``AuthenticationForm`` which adds a remember me
    checkbox.
    
    """
    
    remember_me = forms.BooleanField(label=_('Remember Me'), initial=False,
        required=False)
