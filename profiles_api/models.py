from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings  # Retrieve settings from settings.py file in the Django Project


# Out of the box, Django comes with a default user model, that's used for the standard auth system and also the Django admin.
# We are overriding this model with a custom User model, to user email, instead of the standard username which comes with a default User model.
# We define a CustomUserModel, inherit from AbstractBaseUser and PermissionsMixin, to inherit some methods which are important for auth.
# We need to specify some key implementation details, such as USERNAME_FIELD and REQUIRED_FIELDS

# The UserProfile Class represents user profile objects in the database. The UserProfileManager is used to manage these objects.
# A Manager is the interface through which database query operations are provided to Django models. At least one Manager exists for every model in a Django application.
# The way the manager works, is you specify some functions within the manager that can be used to manipulate objects within the model (object of the database).

# BaseUserManager -> Default User Manager that comes with Django.
# Mark said, that we created a Manager, so Django knows how to work with our custom User Model in the Django CLI Tools. Serializer also uses these methods.
# Serializer will call a create() method of a Model we specified in the Meta Class of the Serializer.

class UserProfileManager(BaseUserManager):
    """ Manager for user profiles """

    # This method is being called by the Serializer in which we pass
    def create_user(self, email, name, password=None):
        """ Create a new user profile """
        if not email:
            raise ValueError('Users must have an email address.')
        email = self.normalize_email(email)  # This function makes sure that the second part of the email is lowercase
        user = self.model(email=email, name=name)
        user.set_password(password)  # This method makes sure that password is encrypted
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

    # What to do when we convert a model instance into a string.
    def __str__(self):
        """ Return a model as a String """
        return self.email


class ProfileFeedItem(models.Model):
    """ Profile status update """
    user_profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    # What to do when we convert a model instance into a string.
    def __str__(self):
        """ Return a model as a String """
        return self.status_text
