# Generated by Django 4.2.4 on 2023-08-23 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0050_reportupdate_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catalogId', models.CharField(blank=True, max_length=256)),
                ('status', models.CharField(blank=True, max_length=256)),
                ('lastUpdate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
