# Generated by Django 4.0.4 on 2023-01-03 17:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='The phone number should look like this: `998901234567`', regex='^(998)\\d{9}$')])),
                ('address', models.TextField(blank=True)),
            ],
        ),
    ]
