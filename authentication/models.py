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

AUTH_PROVIDERS = { 'google': 'google','email': 'email'}


class User(AbstractBaseUser,PermissionsMixin):
    username=models.CharField(max_length=50,unique=True,db_index=True)
    email=models.EmailField(max_length=150,unique=True,db_index=True)
    is_verified=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)

    auth_provider=models.CharField(
        max_length=150,blank=False,
        null=False,default=AUTH_PROVIDERS.get(email))

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']


    objects=UserManager

    def __str__(self):
        return self.email



