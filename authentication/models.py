from django.db import models

from django.utils import timezone

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)

from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


class UserManager(BaseUserManager):

    def create_user(
        self,
        user_type,
        username,
        first_name,
        last_name,
        contact_number,
        email,
        password=None):

        if username is None:
            raise TypeError('Users should have a username')

        if email is None:
            raise TypeError('Users should have a email')

        if user_type >= 1:
            user_type = 1            
        else:
            raise TypeError('Error creating the account. Please, contact the administrator')

        user=self.model(
            user_type=user_type,
            username=username,
            first_name=first_name,
            last_name=last_name,
            contact_number=contact_number,
            email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self,
        username,
        email,
        user_type=1,
        first_name=None,
        last_name=None,
        contact_number=None,
        password=None):

        if password is None:
            raise TypeError('Password should not be None')

        user=self.create_user(
            user_type,
            username,
            first_name,
            last_name,
            contact_number,
            email,
            password)
            
        user.is_superuser=True
        user.is_staff=True
        user.save()
        return user


AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google',
                  'twitter': 'twitter', 'email': 'email'}


class User(AbstractBaseUser, PermissionsMixin):
  
    USER_TYPE_CHOICES = (
      (1, 'normal'),
      (2, 'vip'),
      (3, 'gold'),
      (4, 'platinum'),
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)  
    username=models.CharField(max_length=255, unique=True, db_index=True)
    first_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="First Name")
    last_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Last Name")
    contact_number = models.IntegerField(verbose_name="Contact Number", null=True, blank=True)
    email=models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False, default=AUTH_PROVIDERS.get('email'))
        
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

    objects=UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_companies(self):
        return self.company_set.all()

    def get_reservations(self):
        return self.reservation_set.all()


    def get_imoveis(self):
        return self.imovel_set.all()

    def deassociate_from_companies(self):
        return self.company_set.clear()
