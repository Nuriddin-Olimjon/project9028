# Generated by Django 4.0.4 on 2023-01-03 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_current_role_alter_user_roles'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]
