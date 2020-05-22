from django.db import models
from django.contrib import auth

# Create your models here.

# We are "auth.models.User" to automatically set up a user form.
# self.username is a built in return for "auth.models.User"

class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)

