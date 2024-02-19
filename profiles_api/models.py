from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings


# BaseUserManager -> Default User Manager that comes with Django.
class UserProfileManager(BaseUserManager):
    """ Manager for user profiles """

    def create_user(self, email, name, password=None):
        """ Create a new user profile """
        print('This was called')
        if not email:
            raise ValueError('Users must have an email address.')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """ Create and save a new superuser with given details """
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database model for users in the system """
    email = models.EmailField(max_length=255, unique=True)  # for every emailfield we need to specify max_length
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Because we crated a custom User Model, we need to tell Django how to interact with this User Model, that's why we need to create a Custom Manager.
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'  # We need this to tell Django auth that we want the users to authenticate with their email, instead of username
    REQUIRED_FIELDS = ['name']  # USERNAME_FIELD is required by default

    def get_full_name(self):
        """ Retrieve the full name of the user """
        return self.name

    def get_short_name(self):
        """ Retrieve the short name of the user """
        return self.name

    def __str__(self):
        """ Return a model as a String """
        return self.email


class ProfileFeedItem(models.Model):
    """ Profile status update """
    user_profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Return a model as a String """
        return self.status_text
