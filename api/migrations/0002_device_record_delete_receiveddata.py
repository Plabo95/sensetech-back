# Generated by Django 4.0.5 on 2022-06-07 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('serNo', models.CharField(help_text='Device serial number', max_length=255, primary_key=True, serialize=False, unique=True, verbose_name='serial number')),
                ('iccid', models.CharField(help_text='SIM serial number', max_length=255, verbose_name='SIM serial number')),
                ('imei', models.CharField(help_text='Modem IMEI', max_length=255, verbose_name='Modem IMEI')),
                ('prodId', models.CharField(help_text='Product ID', max_length=255, verbose_name='Product TYPE/ID')),
                ('fw', models.CharField(help_text='Firmware version', max_length=255, verbose_name='Firmware version')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seqNo', models.CharField(help_text='Record sequence number', max_length=255)),
                ('reason', models.CharField(help_text='Reason for logging record', max_length=255)),
                ('dateUTC', models.DateTimeField(help_text='Device UTC datetime', max_length=255)),
                ('lat', models.DecimalField(decimal_places=7, help_text='Latitude', max_digits=12, verbose_name='latitude')),
                ('long', models.DecimalField(decimal_places=7, help_text='Longitude', max_digits=12, verbose_name='longitude')),
                ('alt', models.IntegerField(help_text='Altitude', verbose_name='altitude')),
                ('voltage', models.DecimalField(decimal_places=3, help_text='Battery Voltage in mV ', max_digits=7, verbose_name='voltage')),
                ('temp', models.DecimalField(decimal_places=3, help_text='Temperature Deg C', max_digits=7, verbose_name='temperature')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.device')),
            ],
        ),
        migrations.DeleteModel(
            name='ReceivedData',
        ),
    ]
