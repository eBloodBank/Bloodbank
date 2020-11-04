# Generated by Django 3.1.3 on 2020-11-04 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodPacket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packetID', models.CharField(max_length=70)),
                ('bloodGroup', models.CharField(choices=[('1', 'A+'), ('2', 'A-'), ('3', 'B+'), ('4', 'B-'), ('5', 'AB+'), ('6', 'AB-'), ('7', 'O+'), ('8', 'O-')], max_length=3)),
                ('expiryDate', models.DateField()),
                ('quantity', models.IntegerField(default=250)),
            ],
        ),
        migrations.CreateModel(
            name='BloodBank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('state', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('G', 'Government'), ('R', 'Red Cross'), ('C', 'Charitable'), ('P', 'Private')], max_length=15)),
                ('contactNo', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('PostalAddress', models.CharField(max_length=100)),
                ('BloodPackets', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website_pages.bloodpacket')),
            ],
        ),
    ]
