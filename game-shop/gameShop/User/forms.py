from allauth.account.forms import SignupForm
from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _


class SimpleSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields["email"] = forms.EmailField()

    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    country = forms.CharField()



    def save(self, request):
        user = super(SimpleSignupForm, self).save(request)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.country = self.cleaned_data['country']

        user.save()
        return user

    class Meta:
        model = Account
