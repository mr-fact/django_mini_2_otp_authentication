# Generated by Django 4.2.5 on 2023-09-09 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='otp',
            name='used',
            field=models.BooleanField(default=False),
        ),
    ]
