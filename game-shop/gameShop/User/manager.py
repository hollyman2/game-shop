from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, first_name, last_name, country, date_of_birth, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The email must be set'))
        if not password:
            raise ValueError(_('The password must be set'))
        if not first_name:
            raise ValueError(_('The first_name must be set'))
        if not last_name:
            raise ValueError(_('The last_name must be set'))
        if not country:
            raise ValueError(_('The country must be set'))
        if not date_of_birth:
            raise ValueError(_('The date_of_birth must be set'))

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            country=country,
            date_of_birth=date_of_birth,
            **extra_fields,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        pass
