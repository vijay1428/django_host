# Generated by Django 4.2.4 on 2023-08-03 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0043_customuser_floaterid_customuser_runnerid'),
    ]

    operations = [
        migrations.CreateModel(
            name='FloaterUnitDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deviceId', models.CharField(blank=True, max_length=256)),
                ('status', models.CharField(blank=True, max_length=256)),
                ('lastUpdate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RunnerUnitDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deviceId', models.CharField(blank=True, max_length=256)),
                ('status', models.CharField(blank=True, max_length=256)),
                ('lastUpdate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
