from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password


class CustomUserManager(BaseUserManager):
    def create_user(self, password, is_staff=False, **extra_fields):
        user = self.model(is_staff=is_staff, is_active=True, **extra_fields)

        user.password = make_password(password)
        user.save()

        return user

    def create_superuser(self, password, **extra_fields):
        user = self.create_user(password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user