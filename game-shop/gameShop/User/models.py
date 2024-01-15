from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
    AbstractBaseUser,
)
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
from .manager import CustomUserManager


class Account(AbstractBaseUser):

    validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=30,
        unique=True,
    )

    email = models.EmailField(
        _("email address"),
        unique=True,
    )
    password = models.CharField(
        _('password'),
        max_length=100,
    )
    first_name = models.CharField(
        _("first name"),
        max_length=150,
        validators=[validator],
    )
    last_name = models.CharField(
        _("last name"),
        max_length=150,
        validators=[validator],
    )
    country = models.CharField(
        _('country'),
        max_length=100,
    )
    date_of_birth = models.DateField(
        _('date of birth'),
        default=timezone.now,
    )
    joining_date = models.DateField(
        _("joining date"),
        default=timezone.now,
    )

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        abstract = False

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """ 
        Return the first_name plus the last_name, with a space in between. 
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def user_email(self):
        """Return the email for the user."""
        return self.email

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
