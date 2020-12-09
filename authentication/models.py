from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.



class UserManager(BaseUserManager):
    def create_user(self,email,password=None):
        """
        creates and saves a User with a given mail and password.
        """

        if not mail:
            raise ValueError('Users must have an email address')

        user=self.model(
            email=self.normalize_email(email),
        )


        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

