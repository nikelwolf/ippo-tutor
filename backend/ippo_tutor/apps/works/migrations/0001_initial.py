# Generated by Django 2.1 on 2018-08-28 14:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('tutors', '0001_initial'),
        ('students', '0006_auto_20180827_0716'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('status',
                 models.CharField(choices=[('accepted', 'accepted'), ('to fix', 'to fix'), ('not done', 'not done')],
                                  default='not done', max_length=8)),
                ('file', models.FileField(null=True, upload_to='')),
                ('loaded', models.DateTimeField(auto_now_add=True)),
                ('checked', models.DateTimeField(null=True)),
                ('student',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.StudentProfile')),
                ('subject',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ippo_tutor.apps.works.Subject')),
                ('subject_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                   to='ippo_tutor.apps.works.SubjectType')),
                ('tutor',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tutors.TutorProfile')),
            ],
        ),
    ]
