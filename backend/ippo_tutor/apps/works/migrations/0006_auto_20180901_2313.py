# Generated by Django 2.1 on 2018-09-01 23:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import ippo_tutor.apps.works.models
import ippo_tutor.apps.core.storage


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0005_merge_20180901_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='file',
            field=models.FileField(null=True, storage=ippo_tutor.apps.core.storage.OverwriteStorage(), upload_to=ippo_tutor.apps.core.storage.upload_work, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'zip'])]),
        ),
        migrations.AlterField(
            model_name='work',
            name='student',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='works', to='students.StudentProfile'),
            preserve_default=False,
        ),
    ]
