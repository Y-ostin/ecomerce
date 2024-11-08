from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El Email debe ser provisto")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser debe tener is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"


class ShippingAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_shipping_address")
    address_one = models.CharField(max_length=250, null=True, blank=True)
    address_two = models.CharField(max_length=250, null=True, blank=True)
    zipcode = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "shipping_address"
        verbose_name_plural = "shipping_address"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    mobile_no = models.CharField(null=True, blank=True, max_length=15)
    alt_mobile_no = models.CharField(null=True, blank=True, max_length=15)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "profile"
        verbose_name_plural = "profile"


class ForgotPassword(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_forgot_password")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "forgot_password"
        verbose_name_plural = "forgot_password"
