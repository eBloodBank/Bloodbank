from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, first_name, contact_number, dob, city, blood_group, data_share, username, email, password,
                     **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        user = self.model(first_name=first_name, contact_number=contact_number, dob=dob, city=city,
                          blood_group=blood_group, data_share=data_share, username=username, email=email,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, first_name, contact_number, dob, city, blood_group, data_share, username, email=None,
                    password=None, **extra_fields):
        return self._create_user(first_name, contact_number, dob, city, blood_group, data_share, username, email,
                                 password, **extra_fields)

    def create_superuser(self, first_name, contact_number, dob, city, blood_group, data_share, username, email=None,
                         password=None, **extra_fields):
        return self._create_user(first_name, contact_number, dob, city, blood_group, data_share, username, email,
                                 password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    The user model that in which the user is either a donor or a blood-bank admin
    """
    GENDER = (('M', 'Male'), ('F', 'Female'))
    BLOOD_GROUPS = (
    ('1', 'A+'), ('2', 'A-'), ('3', 'B+'), ('4', 'B-'), ('5', 'AB+'), ('6', 'AB-'), ('7', 'O+'), ('8', 'O-'))

    username = models.CharField(max_length=40, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    email = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=12)
    is_blood_bank_admin = models.BooleanField(default=False)
    is_donor_or_receiver = models.BooleanField(default=True)
    gender = models.CharField(choices=GENDER, max_length=6)
    dob = models.DateField()
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30, null=True, blank=True)
    blood_group = models.CharField(choices=BLOOD_GROUPS, max_length=3)
    number_of_donations = models.IntegerField(default=0)
    data_share = models.BooleanField(default=True)
    is_anonymous = False
    is_authenticated = True
    is_staff = True
    is_superuser = True
    REQUIRED_FIELDS = ['email', 'first_name', 'contact_number', 'dob', 'city', 'blood_group', 'data_share']

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'

    objects = UserManager()

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name
