from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class Theme(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Message(models.Model):
    text = models.TextField()
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    time_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return f'User {self.user.username} wrote: {self.text}'


class MyUserManager(BaseUserManager):

    def _create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields,
        )
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, username, password):
        return self._create_user(email, username, password)

    def create_superuser(self, email, username, password):
        return self._create_user(email, username, password, is_staff=True,
                                 is_active=True, is_superuser=True)


class User(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
