# Generated by Django 4.1.3 on 2023-03-07 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0002_alter_payment_card_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(blank=True, choices=[('mumbai', 'Mumbai'), ('delhi', 'Delhi '), ('bengluru', 'Bengaluru'), ('hydrabad', 'Hyderabad '), ('ahmadabad', 'Ahmadabad'), ('chennai', 'Chennai '), ('kolkata', 'Kolkata '), ('surat', 'Surat '), ('pune', 'Pune '), ('jaipur', 'Jaipur '), ('lucknow', 'Lucknow '), ('nashik', 'Nashik'), ('nagpur', 'Nagpur'), ('indore', 'Indore'), ('thane', 'Thane')], default='mumbai', max_length=50, null=True),
        ),
    ]
