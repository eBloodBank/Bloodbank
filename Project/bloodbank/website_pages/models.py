from django.db import models
from user.models import User

class BloodPacket(models.Model):
    BLOOD_GROUPS = (
    ('1', 'A+'), ('2', 'A-'), ('3', 'B+'), ('4', 'B-'), ('5', 'AB+'), ('6', 'AB-'), ('7', 'O+'), ('8', 'O-'))

    packetID = models.CharField(max_length=70)
    bloodGroup = models.CharField(choices=BLOOD_GROUPS, max_length=3)
    expiryDate = models.DateField()
    quantity = models.IntegerField(default=250)
    Blood_bank = models.ForeignKey('BloodBank', on_delete=models.CASCADE, default="1")

    def __str__(self):
        return self.packetID

class BloodBank(models.Model):
    CATEGORY = (('G', 'Government'), ('R', 'Red Cross'), ('C', 'Charitable'), ('P', 'Private'))

    name = models.CharField(max_length=70)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    category = models.CharField(choices=CATEGORY, max_length=15)
    contactNo = models.CharField(max_length=12)
    email = models.CharField(max_length=50, unique=True)
    PostalAddress = models.CharField(max_length=100)
    BloodPackets = models.ManyToManyField(BloodPacket)
    BloodBankAdmin = models.ForeignKey(User,on_delete=models.CASCADE,default=1)