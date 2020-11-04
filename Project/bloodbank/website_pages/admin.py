from django.contrib import admin
from .models import BloodBank, BloodPacket

admin.site.register(BloodBank)
admin.site.register(BloodPacket)