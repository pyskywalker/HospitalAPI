# Generated by Django 3.2 on 2021-05-19 08:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0007_alter_patient_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='labtestitem',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 5, 19, 8, 23, 15, 420121, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='labtestitem',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='labtestitem',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='diagnoses',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='labtest',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patienttype',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
