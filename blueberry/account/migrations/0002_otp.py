# Generated by Django 4.2.5 on 2023-09-09 10:33

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='phone number must be entered in the (09---------) format ', regex='09\\d{9}')])),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('otp', models.CharField(max_length=15)),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='OTPs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
