# Generated by Django 4.1.7 on 2023-03-06 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pathName', models.CharField(blank=True, max_length=256)),
                ('component', models.CharField(blank=True, max_length=256)),
                ('fileName', models.CharField(blank=True, max_length=256)),
                ('alternetComponent', models.CharField(blank=True, max_length=256)),
                ('status', models.CharField(blank=True, max_length=256)),
                ('lastUpdate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pathName', models.CharField(blank=True, max_length=256)),
                ('component', models.CharField(blank=True, max_length=256)),
                ('fileName', models.CharField(blank=True, max_length=256)),
                ('imagePath', models.CharField(blank=True, max_length=256)),
                ('status', models.CharField(blank=True, max_length=256)),
                ('lastUpdate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]