# Generated by Django 2.1 on 2018-08-30 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0002_auto_20180828_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='tutor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='works', to='tutors.TutorProfile'),
        ),
    ]
