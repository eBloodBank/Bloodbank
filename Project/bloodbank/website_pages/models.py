from django.db import models
from user.models import User

class BloodPacket(models.Model):
    BLOOD_GROUPS = (
    ('1', 'A+'), ('2', 'A-'), ('3', 'B+'), ('4', 'B-'), ('5', 'AB+'), ('6', 'AB-'), ('7', 'O+'), ('8', 'O-'))

    packetID = models.CharField(max_length=70)
    bloodGroup = models.CharField(choices=BLOOD_GROUPS, max_length=3)
    expiryDate = models.DateField()
    quantity = models.IntegerField(default=250)
    Blood_bank = models.ForeignKey('BloodBank', on_delete=models.CASCADE, blank=True,
        null=True)

    def __str__(self):
        return self.packetID
    
    @property
    def quantity_check(self):
        return self.quantity > 0

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
    BloodPackets = models.ManyToManyField(BloodPacket, blank=True)
    BloodBankAdmin = models.ForeignKey(User,on_delete=models.CASCADE)

class BloodDonationEvent(models.Model):
    organizedBy = models.ForeignKey(BloodBank,on_delete=models.CASCADE)
    date = models.DateField()
    venue = models.CharField(max_length=70)
    time = models.CharField(max_length=70)
    campName = models.CharField(max_length=70)
    state = models.CharField(max_length=70)
    district = models.CharField(max_length=70)
    contactNo = models.CharField(max_length=15)