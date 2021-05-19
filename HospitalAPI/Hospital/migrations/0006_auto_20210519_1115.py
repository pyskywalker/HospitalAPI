# Generated by Django 3.2 on 2021-05-19 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0005_patient_is_male'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='diagnoses',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='diagnoses',
            name='diagnoses',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='labtest',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
