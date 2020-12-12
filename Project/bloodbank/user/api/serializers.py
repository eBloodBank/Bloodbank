from rest_framework import serializers
from user.models import User

class ChoiceField(serializers.ChoiceField):

    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        # To support inserts with the value
        if data == '' and self.allow_blank:
            return ''

        for key, val in self._choices.items():
            if val == data:
                return key
        self.fail('invalid_choice', input=data)

class DonorSerializer(serializers.ModelSerializer):
    blood_group = ChoiceField(choices=User.BLOOD_GROUPS)
    
    
    class Meta:
        model = User
        fields = '__all__'
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        print(password)
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.contact_number = validated_data.get('contact_number', instance.contact_number)
        instance.is_blood_bank_admin = validated_data.get('is_blood_bank_admin', instance.is_blood_bank_admin)
        instance.is_donor_or_receiver = validated_data.get('is_donor_or_receiver', instance.is_donor_or_receiver)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.address = validated_data.get('address', instance.address)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.blood_group = validated_data.get('blood_group', instance.blood_group)
        instance.number_of_donations = validated_data.get('number_of_donations', instance.number_of_donations)
        instance.data_share = validated_data.get('data_share', instance.data_share)
        if validated_data.get('password'):
            instance.set_password(validated_data.get('password'))
        instance.save()
        return instance



