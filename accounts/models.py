from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class User(AbstractUser):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(blank=True)
    profile_picture = models.ImageField(upload_to='media/', null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomUserManager()

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
