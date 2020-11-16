from rest_framework import serializers
from .models import BloodBank, BloodPacket, BloodDonationEvent
from user.models import User
from rest_framework.fields import CurrentUserDefault

class BloodPacketSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodPacket
        fields = '__all__'

class BloodDonationEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodDonationEvent
        fields = '__all__'

class BloodBankSerializer(serializers.ModelSerializer):
    BloodPackets = BloodPacketSerializer(many=True)
    class Meta:
        model = BloodBank
        fields = '__all__'

    def create(self, validated_data):
        bloodpackets_data = validated_data.pop('BloodPackets')
        BloodBankz = BloodBank.objects.create(**validated_data)
        user = self.context['request'].user
        #print(user)
        BloodBankz.BloodBankAdmin = user
        BloodBankz.save()
        for bloodpacket_data in bloodpackets_data:
            a = BloodPacket.objects.create(**bloodpacket_data)
            a.Blood_bank = BloodBankz
            a.save()
        setz = BloodPacket.objects.filter(Blood_bank = BloodBankz)
        BloodBankz.BloodPackets.add(*setz)
        return BloodBankz

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.state = validated_data.get('state', instance.state)
        instance.district = validated_data.get('district', instance.district)
        instance.city = validated_data.get('city', instance.city)
        instance.category = validated_data.get('category', instance.category)
        instance.contactNo = validated_data.get('contactNo', instance.contactNo)
        instance.email = validated_data.get('email', instance.email)
        instance.PostalAddress = validated_data.get('PostalAddress', instance.PostalAddress)
        instance.BloodBankAdmin = validated_data.get('BloodBankAdmin', instance.BloodBankAdmin)
        instance.BloodPackets.clear()

        bloodpackets_data = validated_data.pop('BloodPackets') 

        for bloodpacket_data in bloodpackets_data:
            a = BloodPacket.objects.create(**bloodpacket_data)
            a.Blood_bank = instance
            a.save()
            instance.BloodPackets.add(a)

        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'