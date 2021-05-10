# Generated by Django 3.2.2 on 2021-05-10 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Pharmacy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_number', models.IntegerField()),
                ('total_quantity', models.IntegerField()),
                ('order_price', models.FloatField()),
                ('order_date', models.DateTimeField()),
                ('order_status', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='OrderType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('description', models.TextField()),
                ('customer_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sales.order')),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pharmacy.medicine')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='order_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Sales.ordertype'),
        ),
        migrations.AddField(
            model_name='order',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Pharmacy.supplier'),
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_on_invoice', models.DateTimeField(auto_now_add=True)),
                ('total_price', models.FloatField()),
                ('status', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sales.order')),
            ],
        ),
    ]
