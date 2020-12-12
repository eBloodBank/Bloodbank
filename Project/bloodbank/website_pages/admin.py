from django.contrib import admin
from .models import BloodBank, BloodPacket, Order, BloodDonationEvent

admin.site.register(BloodBank)
admin.site.register(BloodPacket)
admin.site.register(Order)
admin.site.register(BloodDonationEvent)