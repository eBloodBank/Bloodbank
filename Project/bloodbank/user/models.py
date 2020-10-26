from django.db import models


class User(models.Model):
    """
    The user model that in which the user is either a donor or a blood-bank admin
    """
    GENDER = (('M', 'Male'), ('F', 'Female'))
    BLOOD_GROUPS = ('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-')
    # user_id = models.IntegerField(max_length=8)
    username = models.CharField(max_length=40)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    contact_number = models.CharField(max_length=12)
    is_blood_bank_admin = models.BooleanField(default=False)
    is_donor_or_receiver = models.BooleanField(default=True)
    gender = models.CharField(choices=GENDER, max_length=6)
    dob = models.DateField()
    address = models.TextField()
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    blood_group = models.CharField(choices=BLOOD_GROUPS, max_length=3)
    number_of_donations = models.IntegerField()
    data_share = models.BooleanField(default=True)
    REQUIRED_FIELDS = [username, first_name, password, contact_number, dob, city, blood_group, data_share]
