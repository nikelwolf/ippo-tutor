# Generated by Django 2.1 on 2018-08-18 05:40

from django.db import migrations
import ippo_tutor.apps.authentication.models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', ippo_tutor.apps.authentication.models.UserManager()),
            ],
        ),
    ]
