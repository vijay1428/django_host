# Generated by Django 4.1.7 on 2023-03-20 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_bannerupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerupdate',
            name='location',
            field=models.ImageField(max_length=1000, upload_to='Banner_image/'),
        ),
    ]
