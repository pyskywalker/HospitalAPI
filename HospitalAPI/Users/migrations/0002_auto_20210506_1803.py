# Generated by Django 3.2.2 on 2021-05-06 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=5)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='usertype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Users.usertype'),
        ),
        migrations.AddField(
            model_name='user',
            name='room',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Users.hospitalroom'),
        ),
    ]