import uuid

from django.contrib.auth.models import AbstractUser,Group
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import EmailValidator, RegexValidator
from django.db import models

from Authentication.validators import validate_lowercase


class UserAccount(AbstractUser):

    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[validate_lowercase]


    )
    email = models.EmailField(
        default=None, blank=True,
        verbose_name='email address',
        max_length=255,
        unique=True,
        validators=[EmailValidator(message='Enter a valid email address.')]
    )
    user_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number= PhoneNumberField()
    otp_enabled = models.BooleanField(default=False)
    otp_base32 = models.CharField(max_length=255, null=True,blank=True)
    otp_auth_url = models.CharField(max_length=255, null=True,blank=True)
    at=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class GroupUser(Group):
    group_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'
